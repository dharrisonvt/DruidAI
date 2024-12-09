import os
import datetime

import IPython
import IPython.display
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import tensorflow as tf
import tensorflow.keras as keras

DATA_PATH = "data/mpi_roof_2023b.csv"
mpl.rcParams['figure.figsize'] = (8, 6)
mpl.rcParams['axes.grid'] = False


data = pd.read_csv(DATA_PATH, encoding="ansi")
data = df[5::6] # Slice down to every 6th record starting from index 5

n = len(data)

data_train = data[0:(0.7 * n)]
data_valid = data[(0.7 * n):(0.9 * n)]
data_test = data[(0.9 * n):]

# Normalization
mean = data_train.mean()
std = data_train.std()
data_train = (data_train - mean) / std
data_valid = (data_valid - mean) / std
data_test = (data_test - mean) / std