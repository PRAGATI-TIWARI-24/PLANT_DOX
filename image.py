
import matplotlib
matplotlib.use('Agg')  # Set backend for headless environment
from matplotlib import pyplot as plt
import numpy as np

# Create a test pattern
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, 'b-', label='Sine wave')
plt.title('Test Visualization')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.legend()
plt.grid(True)

# Save the plot
plt.savefig('test_plot.png')
plt.close()

print("Plot has been saved as 'test_plot.png'")
