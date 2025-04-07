from skimage import io
import numpy as np
from matplotlib import pyplot as plt
my_image= io.imread('uploaded_leaf.jpg')
print(my_image)
random_image = np.random.random([500,500])
plt.imshow(random_image)