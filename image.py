
import matplotlib
matplotlib.use('Agg')  # For headless environments
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import os

try:
    image_path = 'uploaded_leaf.jpg'
    
    # Check if the image exists
    if not os.path.exists(image_path):
        print(f"Error: {image_path} not found in directory: {os.getcwd()}")
        print("Available files:", os.listdir())
        exit(1)
        
    # Load and display the image
    print(f"Loading image from: {image_path}")
    img = Image.open(image_path)
    print(f"Image size: {img.size}")
    print(f"Image mode: {img.mode}")
    
    # Convert to numpy array
    img_array = np.array(img)
    print(f"Array shape: {img_array.shape}")
    
    # Create a figure with larger size and better quality
    plt.figure(figsize=(12, 10))
    plt.imshow(img_array)
    plt.title('Processed Leaf Image')
    plt.axis('off')  # Hide axes
    
    # Save the image with high quality
    output_path = 'output_display.png'
    plt.savefig(output_path, bbox_inches='tight', pad_inches=0, dpi=300, format='png')
    plt.close()
    
    print(f"\nImage successfully processed and saved as '{output_path}'")
    print(f"Output file exists: {os.path.exists(output_path)}")
    print(f"Output file size: {os.path.getsize(output_path)} bytes")
    
except Exception as e:
    print(f"Error processing image: {str(e)}")
    print("Current working directory:", os.getcwd())
    print("Files in directory:", os.listdir())
