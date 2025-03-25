from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Login Form')
root.iconbitmap('favicon.ico')

root.minsize(400,500)
root.configure(background='#1f1f1f')

# Load and resize image
img = Image.open('logo.jpeg')
resized_img = img.resize((80,80), Image.Resampling.LANCZOS)
img = ImageTk.PhotoImage(resized_img)

# Display Image
img_label = Label(root, image=img, bg='#ffffff')
img_label.pack(pady=(35,10))

# Display Heading-Text
text_label = Label(root, text="Capsule Coder", fg='white', bg='red')
text_label.config(font=('cambria', 20))
text_label.pack(pady=2)


#Login Form Begins Here -> For Email:
email_label = Label(root, text='Enter Email', fg='white', bg='#1f1f1f')
email_label.config(font=('georgia', 14))
email_label.pack(pady=(45,10))


#For email input we will use Entry class
email_input = Entry(root, width=45)
email_input.pack(ipady=5, pady=(1,15))


#For Password:
password_label = Label(root, text='Enter Password', fg='white', bg='#1f1f1f')
password_label.pack(pady=(10,10))
password_label.config(font=('georgia', 14))

#For Password Input we will write an Entry class
password_input = Entry(root, width=45)
password_input.pack(ipady=5, pady=(1,15))


#For Submit Button:
login_btn = Button(root, text='Login Here',fg='black', bg='#05a95c', width=15)
login_btn.pack(pady=20)
login_btn.config(font=('georgia', 14))

root.mainloop()