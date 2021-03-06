# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 12:27:06 2022

@author: Ognjen
"""
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend as K
import numpy as np
import matplotlib.pyplot as plt
from keras.preprocessing import image
from tensorflow.keras.preprocessing import image

img_width, img_height = 300, 300
training_dir = 'C:/Users/Ognjen/Desktop/faks/ori/ORI-projekat/basedata/training/'
validation_dir = 'C:/Users/Ognjen/Desktop/faks/ori/ORI-projekat/basedata/validation/'
training_samples = 40
validation_samples =20
epochs = 10
batch_size = 15

if K.image_data_format() == 'channels_first':
    input_shape = (3, img_width, img_height)
else:
    input_shape = (img_width, img_height, 3)
    
training_datagen = ImageDataGenerator(
    rescale = 1. / 255,
    shear_range = 0.2,
    zoom_range = 0.2,
    horizontal_flip = True) 

test_datagen = ImageDataGenerator(rescale = 1. /255)

training_generator = training_datagen.flow_from_directory(
    training_dir,
    target_size = (img_width, img_height),
    batch_size = batch_size,
    class_mode = 'binary'
    )


validation_generator = test_datagen.flow_from_directory(
    validation_dir,
    target_size = (img_width, img_height),
    batch_size = batch_size,
    class_mode = 'binary'
    )



model = Sequential()
model.add(Conv2D(32, (3,3), input_shape = input_shape))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size = (2,2)))

model.summary()

model.add(Conv2D(32, (3,3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size = (2,2)))

model.add(Conv2D(64, (3,3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size = (2,2)))


model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.summary()

model.compile(loss = 'binary_crossentropy',
              optimizer = 'rmsprop',
              metrics=['accuracy'])


model.fit_generator(
    training_generator,
    steps_per_epoch = training_samples // batch_size,
    epochs = epochs,
    validation_data = validation_generator,
    validation_steps = validation_samples //batch_size)

model.save_weights('prvi.h5')

img_pred = image.load_img('C:/Users/Ognjen/Desktop/faks/ori/ORI-projekat/test1.png', target_size = (300,300))
plt.imshow(img_pred)
img_pred = image.img_to_array(img_pred)
img_pred = np.expand_dims(img_pred, axis = 0)



rslt = model.predict(img_pred)

if rslt[0][0] == 1:
    prediction = "latinica"
else:
    prediction = "cirilica"
    
print(prediction)























