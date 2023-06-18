import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

number_of_pixels = 1
number_of_images_selected = 0

selected_pixels = []
selected_pixels_mm = []

def upload_image():
    global number_of_images_selected
    number_of_images_selected += 1
    # Open a file dialog to select an image
    filepath = filedialog.askopenfilename(filetypes=[('Image Files', '*.png;*.jpg;*.jpeg')])
    # enable the select pixel button
    global number_of_pixels
    number_of_pixels = 1
    select_pixel_button.config(state=tk.NORMAL)

    if number_of_images_selected == 2:
        # change the text of the continue button
        continue_button.config(text='Finish')
        

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
    global selected_pixels
    selected_pixels.append((x, y))
    if(globals()['number_of_pixels'] == 1):
        selected_pixel_label_first.config(text=f"Selected Pixel: ({x}, {y})")
    elif(globals()['number_of_pixels'] == 2):
        selected_pixel_label_second.config(text=f"Selected Pixel: ({x}, {y})")
    elif (globals()['number_of_pixels'] == 3):
        selected_pixel_label_third.config(text=f"Selected Pixel: ({x}, {y})")

    canvas.unbind('<Button-1>')  # Disable further pixel selection

    if globals()['number_of_pixels'] == 3:
        select_pixel_button.config(state=tk.DISABLED)
    else:
        globals()['number_of_pixels'] += 1

def continue_to_next_image():
    first_pixel = (int(entry1_1.get()), int(entry1_2.get()))
    second_pixel = (int(entry2_1.get()), int(entry2_2.get()))
    third_pixel = (int(entry3_1.get()), int(entry3_2.get()))

    if first_pixel == ('', '') or second_pixel == ('', '') or third_pixel == ('', ''):
        # pop up
        print('Please select all pixels')
    else:
        print(first_pixel, second_pixel, third_pixel)
        print(selected_pixels)
        selected_pixels_mm.append(first_pixel)
        selected_pixels_mm.append(second_pixel)
        selected_pixels_mm.append(third_pixel)

        # clear the entry
        entry1_1.delete(0, 'end')
        entry1_2.delete(0, 'end')
        entry2_1.delete(0, 'end')
        entry2_2.delete(0, 'end')
        entry3_1.delete(0, 'end')
        entry3_2.delete(0, 'end')

        canvas.image = None

    

# Create the main window
root = tk.Tk()
root.geometry('800x600+400+300')

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

# Create a button to upload the image
upload_button = tk.Button(root, text='Upload Image', command=open_image, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
upload_button.grid(row=2, column=0, sticky='nsew')

# Create a canvas to display the image
canvas = tk.Canvas(root)
vsb = tk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
hsb = tk.Scrollbar(root, orient=tk.HORIZONTAL, command=canvas.xview)
canvas.config(xscrollcommand=hsb.set, yscrollcommand=vsb.set)

# Create a button to select a pixel
select_pixel_button = tk.Button(root, text='Select Pixel', command=lambda: canvas.bind('<Button-1>', select_pixel), bg='brown', fg='white', font=('helvetica', 9, 'bold'), state=tk.DISABLED)
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

selected_pixel_label_first = tk.Label(root, text='First Selected Pixel:')
selected_pixel_label_first.grid(row=1, column=2, sticky='ne')

entry1_1 = tk.Entry(root) 
entry1_1.grid(row=1, column=3, sticky='ne')
entry1_2 = tk.Entry(root)
entry1_2.grid(row=1, column=4, sticky='ne')

selected_pixel_label_second = tk.Label(root, text='Second Selected Pixel:')
selected_pixel_label_second.grid(row=2, column=2, sticky='ne')

entry2_1 = tk.Entry(root) 
entry2_1.grid(row=2, column=3, sticky='ne')
entry2_2 = tk.Entry(root)
entry2_2.grid(row=2, column=4, sticky='ne')

selected_pixel_label_third = tk.Label(root, text='Third Selected Pixel:')
selected_pixel_label_third.grid(row=3, column=2, sticky='ne')

entry3_1 = tk.Entry(root) 
entry3_1.grid(row=3, column=3, sticky='ne')
entry3_2 = tk.Entry(root)
entry3_2.grid(row=3, column=4, sticky='ne')

# continue 
continue_button = tk.Button(root, text='Continue', command=continue_to_next_image, bg='white', fg='brown', font=('helvetica', 9, 'bold'))
continue_button.grid(row=4, column=0, sticky='nsew')


# Run the application
root.mainloop()
