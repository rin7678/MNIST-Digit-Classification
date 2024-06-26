# -*- coding: utf-8 -*-
"""MNIST Digit Classification using Deep Learning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RD1S77VlyhUAi_VuNacGnme8VfKAjMVq

Importing the Dependencies
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import cv2
from google.colab.patches import cv2_imshow
from PIL import Image
import tensorflow as tf
tf.random.set_seed(3)
from tensorflow import keras
from keras.datasets import mnist
from tensorflow.math import confusion_matrix

"""Loading the MNIST Data"""

(X_train, Y_train), (X_test, Y_test) = mnist.load_data()

type(X_train)

# shape of the numpy arrays
print(X_train.shape, Y_train.shape, X_test.shape, Y_test.shape)

"""Training data = 60,000 Images


Test Data = 10,000 Images



Image Dimension = 28 x 28

Grayscale Image = 1 channel ( unlike RGB which has 3 channels)
"""

# printing the 10th image

print(X_train[10])

print(X_train[10].shape)

# displaying the Image

plt.imshow(X_train[26])
plt.show()

# print the corresponding label
print(Y_train[26])

"""Image Label"""

print(Y_train.shape, Y_test.shape)

# unique values in Y_train
print(np.unique(Y_train))

# unique values in Y_test
print(np.unique(Y_test))

"""We can use this label as such or we can also apply One Hot Encoding

All the images have the same dimensions in this dataset , If not, we have to resize all the images to a common dimension
"""

# Scaling the Values
X_train = X_train/255
X_test = X_test/255

# printing the 10th image
print(X_train[10])

"""Building the Neural Network"""

#setting up the layers for a neural network

model = keras.Sequential([

                           keras.layers.Flatten(input_shape=(28, 28)),
                           keras.layers.Dense(50, activation='relu'),
                           keras.layers.Dense(50, activation='relu'),
                           keras.layers.Dense(10, activation='sigmoid')
])

# Compiling the neural Network

model.compile(optimizer='adam',
              loss= 'sparse_categorical_crossentropy',
              metrics=['accuracy'])

# training the neural network

model.fit(X_train, Y_train, epochs=10)

"""Training data accuracy is 98.8 %

**Acuuracy on test data**
"""

loss, accuracy = model.evaluate(X_test, Y_test)

print(accuracy)

"""Test data accuracy is 99.14%"""

print(X_test.shape)

#  first datapoint in X_test
plt.imshow(X_test[0])
plt.show

print(Y_test[0])

Y_pred = model.predict(X_test)

print(Y_pred.shape)

print(Y_pred[0])    #each value show probability of each lable here.

"""model.predict() gives the prediction probability of each class for the particular datapoint

"""

# converting the prediction probabilities to class lables

label_for_first_test_image = np.argmax(Y_pred[0])

print(label_for_first_test_image)

# converting the pediction probabilities to the class label
Y_pred_labels = [np.argmax(i) for i in Y_pred]
print(Y_pred_labels)

print(Y_pred)

"""Y_test -- True Labels

Y_pred_labels -- Predicted Labels

**Confusion Matrix**
"""

conf_mat= confusion_matrix(Y_test, Y_pred_labels)

print(conf_mat)

plt.figure(figsize=(15,7))
sns.heatmap(conf_mat, annot=True, fmt='d', cmap='Blues')
plt.ylabel('True Labels')
plt.xlabel('Predicted Labels')

"""Building a predictive system"""

input_image_path = '/content/MNIST_digit.png'

input_image = cv2.imread(input_image_path)

type(input_image)

print(input_image)

cv2_imshow(input_image)

input_image.shape

grayscale = cv2.cvtColor(input_image, cv2.COLOR_RGB2GRAY)  #this is basically  a color conversion

grayscale.shape

#resizing the image from 318 x 318 to 28 x 28
input_image_resize = cv2.resize(grayscale,(28, 28))

input_image_resize.shape

cv2_imshow(input_image_resize)

input_image_resize = input_image_resize/255

type(input_image_resize)

image_reshape = np.reshape(input_image_resize,[1, 28, 28])

input_prediction = model.predict(image_reshape)
print(input_prediction)

input_pred_label = np.argmax(input_prediction)

print(input_pred_label)

"""**Predictive** **System**"""

input_image_path =  input('Path of the image is to be predicted:')

input_image_path = cv2.imread(input_image_path)

cv2_imshow(input_image)

grayscale = cv2.cvtColor(input_image, cv2.COLOR_RGB2GRAY)

input_image_resize = cv2.resize(grayscale, (28, 28))

input_image_resize = input_image_resize/255

image_reshape = np.reshape(input_image_resize,[1, 28, 28])

input_prediction = model.predict(image_reshape)

input_pred_label = np.argmax(input_prediction)

print('The handwritten digit is recognized as', input_image)

