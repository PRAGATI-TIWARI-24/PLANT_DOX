from skimage import io
import numpy as np 
from matplotlib import pyplot as plt
from skimage import image_as_float
my_image=io.imread('uploaded_leaf.jpg')
print('my_image')
random_image=np.random.random([500,500])
plt.imshow(random_image)
plt.imshow(my_image)
print(random_image.min() , random_image.max())
print(my_image.min() , my_image.max())
