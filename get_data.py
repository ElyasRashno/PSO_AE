import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plot

#dir_name = 'cifar-10-batches-py'
dir_name = 'data'
#dir_name = 'stl10_matlab'

def get_train_data():
    #t_image = np.load('/home/yanan/{}/train_images.npy'.format(dir_name)).astype(np.float32)
    t_image = np.load('{}/train_images.npy'.format(dir_name)).astype(np.float32)
    t_label = np.load('{}/train_labels.npy'.format(dir_name)).astype(np.float32)
    return t_image

def get_validate_data():
    #t_image = np.load('/home/yanan/{}/validate_images.npy'.format(dir_name)).astype(np.float32)
    t_image = np.load('{}/test_28_28_1.npy'.format(dir_name)).astype(np.float32)
    return t_image




