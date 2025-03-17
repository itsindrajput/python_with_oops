from tkinter import *
from PIL import ImageTk, Image

def open_dashboard():

    root.destroy()  # Closes the login window
    dashboard = Tk()
    dashboard.iconbitmap('favicon.ico')
    dashboard.title('Dashboard @ Capsule Coder')
    dashboard.geometry("400x500")
    dashboard.configure(background='#1f1f1f')

    Label(dashboard, text="Welcome to Dashboard", fg='white', bg='#1f1f1f', font=('georgia', 16)).pack(pady=20)
    dashboard.mainloop()

def open_signup():
    root.destroy()

    signup = Tk()
    signup.iconbitmap('favicon.ico')
    signup.title('Sign Up @ Capsule Coder')
    signup.geometry('400x500')
    signup.configure(background='#1f1f1f')

    # Load Image
    img = Image.open('logo.jpeg')
    resized_img = img.resize((80,80), Image.Resampling.LANCZOS)
    signup.img = ImageTk.PhotoImage(resized_img)  # Store image reference

    Label(signup, image=signup.img, bg='#ffffff').pack(pady=(35, 10))
    Label(signup, text="Signup For Capsule Coder", fg='white', bg='red',
          font=('cambria', 18)).pack(pady=2)


    # Create Frame for First and Last Name using Frame
    aframe = Frame(signup, bg='#1f1f1f')
    aframe.pack(pady=(20,0))
    # First Name
    Label(aframe, text="First Name", fg='white', bg='#1f1f1f', font=('georgia', 14)).grid(row=0, column=0, padx=10, pady=3)
    Entry(aframe, width=25).grid(row=1, column=0, padx=12, pady=(5,15))
    # Last Name
    Label(aframe, text="Last Name", fg='white', bg='#1f1f1f', font=('georgia', 14)).grid(row=0, column=1,
                                                                                         padx=10, pady=3)
    Entry(aframe, width=25).grid(row=1, column=1, padx=12, pady=(5,15))

    # Email Id
    Label(aframe, text="Email I'd", fg='white', bg="#1f1f1f", font=('georgia', 14)).grid(row=2, column=0,
                                                                                         padx=10, pady=3)
    Entry(aframe, width=25).grid(row=3, column=0, padx=12, pady=(5,15))
    # Phone Number
    Label(aframe, text="Phone Number", fg='white', bg="#1f1f1f", font=('georgia', 14)).grid(row=2, column=1,
                                                                                            padx=10, pady=3)
    Entry(aframe, width=25).grid(row=3, column=1, padx=12, pady=(5,15))

    # Enter Password
    Label(aframe, text="Enter Password", fg='white', bg="#1f1f1f", font=('georgia', 14)).grid(row=4, column=0,
                                                                                              padx=10, pady=3)
    Entry(aframe, width=25, show='*').grid(row=5, column=0, padx=12, pady=(5,15))
    # Confirm Password
    Label(aframe, text="Confirm Password", fg='white', bg="#1f1f1f", font=('georgia', 14)).grid(row=4, column=1,
                                                                                                padx=10, pady=3)
    Entry(aframe, width=25, show='*').grid(row=5, column=1, padx=12, pady=(5,15))

    Button(signup, text='Create Account', fg='black', bg='#4fa261', width=30, height=1, font=('georgia', 14),
                    command=open_signup).pack(pady=(10,0))

    signup.mainloop()

root = Tk()
root.title('Login @ Capsule Coder')
root.iconbitmap('favicon.ico')

root.minsize(400, 500)
root.configure(background='#1f1f1f')

# Load and resize image
img = Image.open('logo.jpeg')
resized_img = img.resize((80, 80), Image.Resampling.LANCZOS)
img = ImageTk.PhotoImage(resized_img)

# Display Image
img_label = Label(root, image=img, bg='#ffffff')
img_label.pack(pady=(35, 10))

# Display Heading-Text
text_label = Label(root, text="Login Here", width=10, height=1, fg='white', bg='red', font=('cambria', 20))
text_label.pack(pady=2)

# Login Form Begins Here -> For Email:
email_label = Label(root, text='Enter Your Email', fg='white', bg='#1f1f1f', font=('georgia', 14))
email_label.pack(pady=(45, 10))

email_input = Entry(root, width=45)
email_input.pack(ipady=5, pady=(1, 15))

# For Password:
password_label = Label(root, text='Enter Password', fg='white', bg='#1f1f1f', font=('georgia', 14))
password_label.pack(pady=(10, 10))

password_input = Entry(root, width=45, show="*")  # Hides password input
password_input.pack(ipady=5, pady=(1, 15))

# Create a frame for buttons (side-by-side layout)
btn_frames = Frame(root, bg='#1f1f1f')
btn_frames.pack(pady=20)

# For Login Button:
login_btn = Button(btn_frames, text='LogIn', fg='black', bg='#05a95c', width=8, height=1, font=('georgia', 14),
                   command=open_dashboard)
login_btn.grid(row=0, column=0, padx=10)

# For Signup Button:
signup_btn = Button(btn_frames, text='SignUp', fg='black', bg='#4fa261', width=8, height=1, font=('georgia', 14),
                    command=open_signup)
signup_btn.grid(row=0, column=1, padx=10)

root.mainloop()
