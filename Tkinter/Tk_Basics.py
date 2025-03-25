#Step 1: 
"""
from tkinter import *
root = Tk()
root.mainloop()
"""



"""
from tkinter import *
root = Tk()
root.title('Login Form')
root.iconbitmap('favicon ico')
root.minsize(300,300)
# root.maxsize(300,300)
root.geometry('350x450')
root.configure(background = '#101010')
root.mainloop()
"""



#Step 2: Install pillow library to add image in Gui of Tkinter: pip install pillow
"""
from tkinter import *
from PIL import ImageTk, Image
import os
root = Tk()
root.title('Login Form')
root.iconbitmap('favicon ico')
root.minsize(300,300)
root.geometry('350x450')
root.configure(background = '#101010')

img = ImageTk.PhotoImage(Image.open(file='logo.jpeg')) 
"""
"""
# To place the above image on our GUI screen we will use a Label 
# Generally label is used to print the text on the GUI Screen but we use the Label to print the images as well.
# And everytime we create a Label we have to explicitly tell it sit over the GUI and to achieve this we will use a geometry manager.
# A Geometry manager will decide which component will be placed to which part of the screen. (act as an interior designer)

Tkinter offers three geometry managers for arranging widgets: pack, grid, and place, each with distinct strengths for different layout needs. 
Pack:
Organizes widgets in blocks, stacking them along the parent widget's sides (top, bottom, left, or right). It's good for simple layouts and stacking widgets. 
Grid:
Places widgets in a grid-like structure, allowing for precise positioning using rows and columns. It's suitable for creating complex, table-like layouts. 
Place:
Provides absolute control over widget positioning by specifying exact x and y coordinates. It's useful when neither grid nor pack is suitable. 
"""
"""
img_label = Label(root,image=img)
root.mainloop()
"""




from tkinter import *
from PIL import ImageTk, Image
import os # Import the os module

root = Tk()
root.title('Login Form')
root.minsize(300, 300)
root.geometry('350x450')
root.configure(background='#101010')

try:
    # Construct the full path to the image file.
    script_dir = os.path.dirname(os.path.abspath(__file__)) # Get the directory of the current script
    image_path = os.path.join(script_dir, 'logo.jpeg') # Combine the script directory and image filename.

    img = ImageTk.PhotoImage(Image.open(image_path))
    img_label = Label(root, image=img, bg='#101010') # Add background to the label to match root.
    img_label.pack(pady=20) # Use pack to place the label, add padding for visual separation

except FileNotFoundError:
    print("Error: logo.jpeg not found.")
    error_label = Label(root, text="Image not found", fg="red", bg='#101010')
    error_label.pack(pady=20)

root.mainloop()