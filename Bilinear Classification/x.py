import numpy as np
import matplotlib.pyplot as plt
import h5py
import scipy
from PIL import Image
from scipy import ndimage
# from lr_utils import load_dataset
# Loading the datasets---
train_ds = h5py.File('datasets/train_catvnoncat.h5',"r")

print(train_ds)
