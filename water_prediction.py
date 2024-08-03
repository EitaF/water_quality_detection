#Import modules
import os
import sys
import shutil
import random
import cv2
import tensorflow as tf
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.models import Sequential, load_model, Model
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Input
from tensorflow.keras.preprocessing.image import array_to_img, img_to_array, load_img, ImageDataGenerator
from tensorflow.keras import optimizers
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping
from keras.applications.vgg16 import VGG16
import numpy as np
import matplotlib.pyplot as plt

#Load trained vgg model
def load_vggmodel(h5file):
    model = load_model(h5file)
    return model

#Resize jpeg image to fit the model
def predicted_image(jpgimage):
    image = cv2.imread(jpgimage)
    image = cv2.resize(image, (224, 224))
    return image

if __name__ == "__main__":
    """
    Load trained model as h5file and load jpeg image.
    Judge OK / NG by prediction. Float value is returned. OK is close to 1. NG is close to 0.
    """
    def prediction(h5file, image):
        model = load_vggmodel(h5file)
        image = predicted_image(image)
        predicted_result = model.predict(image.reshape(-1, 224, 224, 3))
        return predicted_result
