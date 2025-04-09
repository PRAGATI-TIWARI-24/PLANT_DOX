
from skimage import io
from PIL import Image
import numpy as np 
from matplotlib import pyplot as plt
my_image=io.imread('uploaded_leaf.jpg')
print('my_image')
random_image=np.random.random([200,200])
print(my_image.size)
print(my_image.dtype)
print(my_image.shape)
