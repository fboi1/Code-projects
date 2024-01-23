
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
import numpy as np
#import seaborn as sns
df = pd.read_csv(r"C:\firaas\code\jena_climate_2009_2016.csv")




# Slice [start:stop:step], starting from index 5 take every 6th record then we will have hourly data




#replace -99999 wv and maxwv values with 0 ====
wv = df['wv (m/s)']
bad_wv = wv == -9999.0
wv[bad_wv] = 0.0

max_wv = df['max. wv (m/s)']
bad_max_wv = max_wv == -9999.0
max_wv[bad_max_wv] = 0.0

# The above inplace edits are reflected in the DataFrame.
df['wv (m/s)'].min()
#=========
#wind is from 0 to 360 degrees so convert it into a vector with wind velocity ===
wv = df.pop('wv (m/s)')
max_wv = df.pop('max. wv (m/s)')

# Convert to radians.
wd_rad = df.pop('wd (deg)')*np.pi / 180

# Calculate the wind x and y components.
df['Wx'] = wv*np.cos(wd_rad)
df['Wy'] = wv*np.sin(wd_rad)

# Calculate the max wind x and y components.
df['max Wx'] = max_wv*np.cos(wd_rad)
df['max Wy'] = max_wv*np.sin(wd_rad)

#====================================

#parameters
step = 6 #taking every 6th row yeilds hourly values

past = 720 # window will take past 720 values
future = 72 # and forecast 72 values ahead
#since it's per 6 steps its actually 720/6 = 120 values back and 72/6 = 12 values forward

learning_rate = 0.001
batch_size = 256
epochs = 10


feature_keys = [
    "p (mbar)",
    "T (degC)",
    "Tpot (K)",
    "Tdew (degC)",
    "rh (%)",
    "VPmax (mbar)",
    "VPact (mbar)",
    "VPdef (mbar)",
    "sh (g/kg)",
    "H2OC (mmol/mol)",
    "rho (g/m**3)",
    "Wx",
    "Wy",
    "max. wv (m/s)",
    "wd (deg)",
]



wantedcolumns_index = [0, 1, 5, 7, 8, 10, 11, 12] #included wx and wy unlike example

wantedcolumns = [feature_keys[i] for i in wantedcolumns_index]
features = df[wantedcolumns]


def normalize(data, train_split):
    data_mean = data[:train_split].mean(axis=0)
    data_std = data[:train_split].std(axis=0)
    return (data - data_mean) / data_std # returns array
 
train_split = int(0.715 * int(df.shape[0]))
features = normalize(features.values, train_split)
features = pd.DataFrame(features)




n = len(df)
train_df = features[0:int(n*0.715)] #first 71.5%
val_df = features[int(n*0.715):] #after first 71.5%


train_mean = train_df.mean()
train_std = train_df.std()
#normalised train and val df
train_df = (train_df - train_mean) / train_std
val_df = (val_df - train_mean) / train_std






#train
start = past + future
end = start + train_df.shape[0]





#train data windows
x_train = train_df.iloc[:,[0,1,2,3,4,5,6,7]].values #convert to array - columns needed for train
y_train = train_df.iloc[start:end,[1]] # https://www.codegrepper.com/code-examples/python/select+column+without+name+pandas - labelled columns for train

sequence_length = int(past / step) # 120

from tensorflow.keras.preprocessing import timeseries_dataset_from_array
dataset_train = timeseries_dataset_from_array(
    x_train,
    y_train,
    sequence_length=sequence_length,
    sampling_rate=step,
    batch_size=batch_size,
)


for batch in dataset_train.take(1):
    inputs, targets = batch

print("Input shape:", inputs.numpy().shape)
print("Target shape:", targets.numpy().shape)


#val data windows
x_end = len(val_df) - past - future
label_start = train_df.shape[0] + past + future
x_val = val_df.iloc[:x_end,[0,1,2,3,4,5,6,7]].values
y_val = features.iloc[label_start:,[1]]

dataset_val = timeseries_dataset_from_array(
    x_val,
    y_val,
    sequence_length=sequence_length,
    sampling_rate=step,
    batch_size=batch_size,
)

#initialise model - functional api not sequence
from keras import layers
from keras import Model
from tensorflow.keras.optimizers import Adam #
from keras import callbacks

inputs = layers.Input(shape=(inputs.shape[1], inputs.shape[2]))
lstm_out = layers.LSTM(32)(inputs)
outputs = layers.Dense(1)(lstm_out)
model = Model(inputs=inputs, outputs=outputs)
model.compile(optimizer=Adam(learning_rate=learning_rate), loss="mse")
print(model.summary())

#fit with checkpoints
path_checkpoint = "model_checkpoint.h5"
es_callback = callbacks.EarlyStopping(monitor="val_loss", min_delta=0, patience=5)

modelckpt_callback = callbacks.ModelCheckpoint(
    monitor="val_loss",
    filepath=path_checkpoint,
    verbose=1,
    save_weights_only=True,
    save_best_only=True,
)

history = model.fit(
    dataset_train,
    epochs=epochs,
    validation_data=dataset_val,
    callbacks=[es_callback, modelckpt_callback],
)

#view loss
def visualize_loss(history, title):
    loss = history.history["loss"]
    val_loss = history.history["val_loss"]
    epochs = range(len(loss))
    plt.figure()
    plt.plot(epochs, loss, "b", label="Training loss")
    plt.plot(epochs, val_loss, "r", label="Validation loss")
    plt.title(title)
    plt.xlabel("Epochs")
    plt.ylabel("Loss")
    plt.legend()
    plt.show()


visualize_loss(history, "Training and Validation Loss")
plt.show()