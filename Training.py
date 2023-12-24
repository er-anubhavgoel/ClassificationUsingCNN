import tensorflow as tf
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.callbacks import TensorBoard
import pickle
import time

NAME = "Metals-vs-Plastics-cnn-64x2-{}".format(int(time.time()))
tensorboard = TensorBoard(log_dir='logs/{}'.format(NAME))

X=np.array(pickle.load(open("X.pickle", "rb")))     #Image Extraction
y=np.array(pickle.load(open("y.pickle", "rb")))     #Image Labels

X = X/255.0         #Used for normalising image in X due to RGB extraction to Gray,and (Standardisatiion ranging between 0 & 1)

model = Sequential()        #General Model with no Back-Propagation

model.add(Conv2D((64),(3,3),input_shape=X.shape[1:]))   #64 feature detectors, 3x3 matrix
model.add(Activation("relu"))                           #Hidden Layer-1
model.add(MaxPooling2D(pool_size=(2,2)))                #Resultant matrix of 2x2 is made by maxpool

model.add(Conv2D((64),(3,3),input_shape=X.shape[1:]))   #3 rows and 3 columns
model.add(Activation("relu"))                           #Hidden Layer-2
model.add(MaxPooling2D(pool_size=(2,2)))                #For No data loss

model.add(Flatten())        #Conversion of 2D array into single 1D vector

model.add(Dense(64))        #64 Neurons in each Hidden Layer connected to previous and subsequent layers

model.add(Dense(1))                             #Output Layer
model.add(Activation('sigmoid'))                #Output Layer

model.compile(loss="binary_crossentropy",
              optimizer="adam",
              metrics=['accuracy'])

model.fit(X, y, batch_size=300, epochs=10, validation_split=0.1, callbacks=[tensorboard])
#(300 images for one epoch, 0.1=10% Data stored for Future Testing being a supervised learning model)

print()
scores = model.evaluate(X, y)
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
print()
model.save("MPmodel.h5")
print("Saved model to disk")
