import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

number_of_pixels = 3

def upload_image():
    filepath = filedialog.askopenfilename(filetypes=[('Image Files', '*.png;*.jpg;*.jpeg')])
    return filepath

def open_image():
    # Get the file path from the upload_image() function
    filepath = upload_image()

    # Open the image
    image = Image.open(filepath)

    # Display the image
    display_image = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor='nw', image=display_image)
    canvas.image = display_image
    canvas.config(scrollregion=(0, 0, display_image.width(), display_image.height()))

    canvas.focus_set()

# def zoom(event):
#     scale_factor = 1.2 if event.delta > 0 else 0.8
#     # Adjust the zoom level based on the scroll direction
#     if event.delta > 0:
#         scale_factor *= 1.1
#     else:
#         scale_factor /= 1.1

#     # Resize the canvas based on the new scale factor
#     canvas.scale("all", 0, 0, scale_factor, scale_factor)
#     canvas.configure(scrollregion=canvas.bbox("all"))

def scroll_horizontal(dx):
  canvas.xview_scroll(dx, 'units')

def scroll_vertical(dy):
  canvas.yview_scroll(dy, 'units')

def show_pixel(event):
    x = canvas.canvasx(event.x)  # Get the actual x coordinate on the image
    y = canvas.canvasy(event.y)
    pixel_location_label.config(text=f"Pixel Location: ({x}, {y})")

    # Process the selected pixel
    # Add your pixel selection logic here

def select_pixel(event):
    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)
    print(f"Selected Pixel: ({x}, {y})")
    selected_pixel_label.config(text=f"Selected Pixel: ({x}, {y})")
    canvas.unbind('<Button-1>')  # Disable further pixel selection

    if globals()['number_of_pixels'] <= 0:
        select_pixel_button.config(state=tk.DISABLED)
    else:
        globals()['number_of_pixels'] -= 1

# Create the main window
root = tk.Tk()
root.geometry('800x600+400+300')

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

# Create a button to upload the image
upload_button = tk.Button(root, text='Upload Image', command=open_image)
upload_button.grid(row=2, column=0, sticky='nsew')

# Create a canvas to display the image
canvas = tk.Canvas(root)
vsb = tk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
hsb = tk.Scrollbar(root, orient=tk.HORIZONTAL, command=canvas.xview)
canvas.config(xscrollcommand=hsb.set, yscrollcommand=vsb.set)

# Create a button to select a pixel
select_pixel_button = tk.Button(root, text='Select Pixel', command=lambda: canvas.bind('<Button-1>', select_pixel))
select_pixel_button.grid(row=3, column=0, sticky='nsew')

canvas.grid(row=0, column=0, sticky='nsew')
vsb.grid(row=0, column=1, sticky='ns')
hsb.grid(row=1, column=0, sticky='ew')

# For the canvas to be scrollable, and to be able to zoom in and out, we need to add a frame
canvas.config(scrollregion=canvas.bbox("all"))

# canvas.bind('<MouseWheel>', lambda e: scroll_vertical(-e.delta//120))
# canvas.bind('<Button-1>', select_pixel)
canvas.bind('<Motion>', show_pixel)

canvas.bind('<Up>', lambda e: scroll_vertical(-1))
canvas.bind('<Down>', lambda e: scroll_vertical(+1))
canvas.bind('<Left>', lambda e: scroll_horizontal(-1))
canvas.bind('<Right>', lambda e: scroll_horizontal(+1))

pixel_location_label = tk.Label(root, text='Pixel Location:')
pixel_location_label.grid(row=0, column=2, sticky='ne')

selected_pixel_label = tk.Label(root, text='First Selected Pixel:')
selected_pixel_label.grid(row=1, column=2, sticky='ne')

selected_pixel_label = tk.Label(root, text='Second Selected Pixel:')
selected_pixel_label.grid(row=2, column=2, sticky='ne')

selected_pixel_label = tk.Label(root, text='Third Selected Pixel:')
selected_pixel_label.grid(row=3, column=2, sticky='ne')
# Run the application
root.mainloop()
