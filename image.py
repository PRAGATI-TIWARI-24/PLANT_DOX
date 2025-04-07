
import matplotlib
matplotlib.use('Agg')  # Set backend for headless environment
from matplotlib import pyplot as plt
from skimage import io
import numpy as np

my_image = io.imread('uploaded_leaf.jpg')
plt.imshow(my_image)
plt.axis('off')
plt.savefig('processed_leaf.png')  # Save the plot instead of displaying it
plt.close()
