import numpy as np
import matplotlib.pyplot as plt

# Define the range of x values from -2π to 2π
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

# Calculate the sine of x
y = np.sin(x)

# Create the plot
plt.figure(figsize=(10, 5))
plt.plot(x, y, label='Sine Wave', color='blue')

# Add title and labels
plt.title('Sine Wave from -2π to 2π')
plt.xlabel('x (radians)')
plt.ylabel('sin(x)')
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()

# Save the plot as a PNG file
plt.savefig('sine_wave.png')
plt.close()  # Close the plt to prevent it from displaying in some environments