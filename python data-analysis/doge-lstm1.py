#%%
from re import X
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
import numpy as np
#import seaborn as sns
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

df = pd.read_csv(r"C:\firaas\code\cleandcsv30.csv")

#=
split_fraction = 0.715
train_split = int(split_fraction * int(df.shape[0]))

#=

#parameters
step = 1 #taking every 6th row yeilds hourly values

past = 720 # window will take past 720 values
future = 72 # and forecast 72 values ahead
#since it's per 6 steps its actually 720/6 = 120 values back and 72/6 = 12 values forward

learning_rate = 0.001
batch_size = 256
epochs = 10


feature_keys = ['time', 'bid/ask', 'price-ETH', 'volb-ETH', 'volq-ETH', 'price-doge',
       'volb-doge', 'volq-doge', 'fee', 'total-val', 'total-fee',
       'total-bin-tx-val', 'change'
]

def normalize(data, train_split):
    data_mean = data[:train_split].mean(axis=0)
    data_std = data[:train_split].std(axis=0)
    return (data - data_mean) / data_std # returns array


wantedcolumns_index = [0,1,2,3,4,5,6,7,8,9,11,12] #included wx and wy unlike example

wantedcolumns = [feature_keys[i] for i in wantedcolumns_index]
features = df[wantedcolumns]
features.index = features['time']
features.pop('time')




features = normalize(features.values, train_split)
features = pd.DataFrame(features)
print(features.head(20))




train_data = features.loc[0 : train_split - 1]
val_data = features.loc[train_split:]


train_mean = train_data.mean()
train_std = train_data.std()
#normalised train and val df
train_data = (train_data - train_mean) / train_std
val_data = (val_data - train_mean) / train_std

#train
start = past + future
end = start + train_split

print(train_data.head())



#train data windows
x_train = train_data[[i for i in range(10)]].values
print(x_train)
y_train = features.iloc[start:end][[4]]


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
x_end = len(val_data) - past - future
label_start = train_split + past + future
x_val = val_data.iloc[:x_end][[i for i in range(10)]].values
y_val = features.iloc[label_start:][[4]]
dataset_val = keras.preprocessing.timeseries_dataset_from_array(
    x_val,
    y_val,
    sequence_length=sequence_length,
    sampling_rate=step,
    batch_size=batch_size,
)

for batch in dataset_train.take(1):
    inputs, targets = batch

#=========================================================!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
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
#%%