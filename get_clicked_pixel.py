import matplotlib.pyplot as plt
import numpy as np

def onclick(event):
    if event.button == 1:  # Left mouse button
        x, y = int(event.xdata), int(event.ydata)
        print("Clicked pixel location: ({}, {})".format(x, y))

        # Create a copy of the image to modify
        modified_image = np.copy(image)

        # Change color to red (10x10 pixels)
        modified_image[y:y+10, x:x+10] = [255, 0, 0]  # RGB value for red

        # Refresh the plot with the modified image
        ax.imshow(modified_image)
        plt.draw()

image_path = r"Kontrol Kart 1\5RC_6007.jpg"

# Read the image
image = plt.imread(image_path)

# Display the image
fig, ax = plt.subplots()
ax.imshow(image)

# Connect the click event handler
cid = fig.canvas.mpl_connect('button_press_event', onclick)

# Show the plot
plt.show()
