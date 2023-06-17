import matplotlib.pyplot as plt

def onclick(event):
    if event.button == 1:  # Left mouse button
        x, y = int(event.xdata), int(event.ydata)
        print("Clicked pixel location: ({}, {})".format(x, y))

        # Change color to red (10x10 pixels)
        image[y:y+100, x:x+100] = [255, 0, 0]  # RGB value for red

        # Refresh the plot
        ax.imshow(image)
        plt.draw()

# Read the image
image = plt.imread(r"Kontrol Kart 1\5RC_6009.jpg")

# Display the image
fig, ax = plt.subplots()
ax.imshow(image)

# Connect the click event handler
cid = fig.canvas.mpl_connect('button_press_event', onclick)

# Show the plot
plt.show()
