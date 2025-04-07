
import matplotlib
matplotlib.use('Agg')  # For headless environments
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import os

try:
    # Check if the image exists
    if not os.path.exists('uploaded_leaf.jpg'):
        print("Error: uploaded_leaf.jpg not found")
        exit(1)
        
    # Load and display the image
    img = Image.open('uploaded_leaf.jpg')
    
    # Convert to numpy array
    img_array = np.array(img)
    
    # Create a figure
    plt.figure(figsize=(10, 8))
    plt.imshow(img_array)
    plt.axis('off')  # Hide axes
    
    # Save the image
    plt.savefig('output_display.png', bbox_inches='tight', pad_inches=0, dpi=300)
    plt.close()
    
    print("Image has been processed and saved as 'output_display.png'")
    
except Exception as e:
    print(f"Error processing image: {str(e)}")
