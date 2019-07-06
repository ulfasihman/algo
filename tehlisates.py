# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 19:15:45 2019

@author: Ulfa
"""

import numpy as np
import matplotlib.pylab as plt
import tensorflow as tf
from keras.models import Model, Sequential
from keras.layers import Input, Activation, Dense
from keras.optimizers import SGD

# Generate data from -20, -19.75, -19.5, .... , 20
"""train_x = np.arange(-20, 20, 0.25)"""
train_x = np.array([2])

# Calculate Target : sqrt(2x^2 + 1)
train_y = np.sqrt((2*train_x**2)+1)
print (train_y)
