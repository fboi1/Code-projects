#https://stackoverflow.com/questions/67604780/unable-to-import-sgd-and-adam-from-keras-optimizers helps for importing error
import tensorflow as tf
from tensorflow import keras
from keras.models import load_model
from keras import layers
import numpy as np
#load model 
newload = load_model(r'./1655586185.h5')
print(newload.summary())
#predict from the model
print(newload.predict([100]))
#can also continue to train it with fit method
celciusq = np.array([-40,-10,0,8,15,22,38,64], dtype=float)
farenheighta = np.array([-40,14,32,46,59,72,100,147], dtype=float)
history = newload.fit(celciusq, farenheighta, epochs = 2, verbose = False)
print(newload.predict([100]))

