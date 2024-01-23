
#https://stackoverflow.com/questions/67604780/unable-to-import-sgd-and-adam-from-keras-optimizers helps for import problems
import tensorflow as tf
import numpy as np
import keras
celciusq = np.array([-40,-10,0,8,15,22,38], dtype=float)
farenheighta = np.array([-40,14,32,46,59,72,100], dtype=float)

#idx is index, x is celciusq value
for idx, x in np.ndenumerate(celciusq):
  print("{}, {}".format(x, farenheighta[idx])) 

#import keras stuff  
from keras import layers
from keras import models
from keras import optimizers
from tensorflow.keras.optimizers import Adam
Dense = layers.Dense

#define model
#x is one layer, with num of units as neurons... and input shape is shape 1d array(?)
x = Dense(units=1, input_shape = [1])
model = models.Sequential(x)

#compile to find best model using mse, learning rate is learning rate
# model.compile(losee='mean_squared_error',optimizer=optimizers.adam_v2(0.1))
model.compile(loss='mean_squared_error',optimizer=Adam(0.1))

#train
history = model.fit(celciusq, farenheighta, epochs = 500, batch_size = 4, verbose = False)

import matplotlib.pyplot as plt
plt.xlabel = ('epoch number')
plt.ylabel = ('loss magnitude')
plt.plot(history.history['loss'])
#plt.show()
print(model.predict([100]))
#check weights
print("weights:")
print(model.get_weights())


#saving model
#get time rn
import time
t= time.time()
#save filename as the current time
export_path = "./{}.h5".format(int(t))
print(export_path)
#model.save(export_path)
