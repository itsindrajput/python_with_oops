import json
from tkinter import *
from PIL import ImageTk, Image
import os

USER_FILE = "users.json"

if os.path.exists(USER_FILE):
    with open(USER_FILE, "r") as file:
        user_data = json.load(file)
else:
    user_data = {}

def save_user_data():
    with open(USER_FILE, "w") as file:
        json.dump(user_data, file, indent=4)

def open_login():
    signup.destroy()
    main_screen()

def open_dashboard():
    root.destroy()
    dashboard = Tk()
    dashboard.iconbitmap('favicon.ico')
    dashboard.title('Dashboard @ Capsule Coder')
    dashboard.geometry('420x540')
    dashboard.configure(background='#202020')

    img = Image.open('logo.jpeg')
    resized_img = img.resize((80, 80), Image.Resampling.LANCZOS)
    dashboard.img = ImageTk.PhotoImage(resized_img)
    Label(dashboard, image=dashboard.img, bg='#202020').pack(pady=20)
    
    Label(dashboard, text="Welcome to Dashboard", fg='white', bg='#202020', font=('Georgia', 18, 'bold')).pack(pady=10)
    Button(dashboard, text='Logout', fg='white', bg='red', width=12, font=('Georgia', 14, 'bold'), relief=FLAT, command=dashboard.destroy).pack(pady=20)
    dashboard.mainloop()

def open_signup():
    global signup, first_name, last_name, email, phone, password, confirm_password, signup_msg
    root.destroy()
    signup = Tk()
    signup.iconbitmap('favicon.ico')
    signup.title('Sign Up @ Capsule Coder')
    signup.geometry('420x570')
    signup.configure(background='#1f1f1f')

    img = Image.open('logo.jpeg')
    resized_img = img.resize((80,80), Image.Resampling.LANCZOS)
    signup.img = ImageTk.PhotoImage(resized_img)
    Label(signup, image=signup.img, bg='#1f1f1f').pack(pady=20)
    
    Label(signup, text="Signup for Capsule Coder", fg='white', bg='#ff4757', font=('Cambria', 18, 'bold')).pack(pady=10)
    
    def create_input(parent, label, show=''):
        Label(parent, text=label, fg='white', bg='#1f1f1f', font=('Georgia', 11)).pack(anchor=W, padx=20, pady=3)
        entry = Entry(parent, width=30, font=('Georgia', 12), show=show, bg='#292929', fg='white', insertbackground='white', relief=FLAT)
        entry.pack(padx=20, pady=5, ipady=6, fill=X)
        return entry
    
    first_name = create_input(signup, "First Name")
    last_name = create_input(signup, "Last Name")
    email = create_input(signup, "Email ID")
    phone = create_input(signup, "Phone Number")
    password = create_input(signup, "Enter Password", show='*')
    confirm_password = create_input(signup, "Confirm Password", show='*')

    signup_msg = Label(signup, text="", fg='white', bg='#1f1f1f', font=('Georgia', 12))
    signup_msg.pack()
    
    def create_account():
        email_text = email.get()
        if email_text in user_data:
            signup_msg.config(text="Email already exists!", fg='red')
        elif password.get() != confirm_password.get():
            signup_msg.config(text="Passwords do not match!", fg='red')
        else:
            user_data[email_text] = password.get()
            save_user_data()
            signup_msg.config(text="Account Created Successfully!", fg='green')
    
    Button(signup, text='Create Account', fg='white', bg='#2ecc71', width=30, height=2, font=('Georgia', 14, 'bold'), relief=FLAT, command=create_account).pack(pady=10)
    Button(signup, text='Back to Login', fg='white', bg='#3498db', width=30, height=2, font=('Georgia', 14, 'bold'), relief=FLAT, command=open_login).pack(pady=10)
    signup.mainloop()

def validate_login():
    email_text = email_input.get()
    if email_text in user_data and user_data[email_text] == password_input.get():
        open_dashboard()
    else:
        login_msg.config(text="Invalid Credentials!", fg='red')

def main_screen():
    global root, email_input, password_input, login_msg
    root = Tk()
    root.title('Login @ Capsule Coder')
    root.iconbitmap('favicon.ico')
    root.minsize(420, 550)
    root.configure(background='#1f1f1f')
    
    img = Image.open('logo.jpeg')
    resized_img = img.resize((80, 80), Image.Resampling.LANCZOS)
    img = ImageTk.PhotoImage(resized_img)
    Label(root, image=img, bg='#1f1f1f').pack(pady=20)
    
    Label(root, text="Login Here", fg='white', bg='#ff4757', font=('Cambria', 20, 'bold')).pack(pady=10)
    
    email_label = Label(root, text='Enter Your Email', fg='white', bg='#1f1f1f', font=('georgia', 14))
    email_label.pack(pady=(20,0))

    email_input = Entry(root, width=40, font=('Georgia', 12), bg='#292929', fg='white', insertbackground='white', relief=FLAT)
    email_input.pack(ipady=8, pady=5, padx=20, fill=X)
    
    # For Password:
    password_label = Label(root, text='Enter Password', fg='white', bg='#1f1f1f', font=('georgia', 14))
    password_label.pack(pady=(10,0))

    password_input = Entry(root, width=40, font=('Georgia', 12), show='*', bg='#292929', fg='white', insertbackground='white', relief=FLAT)
    password_input.pack(ipady=8, pady=5, padx=20, fill=X)
    
    login_msg = Label(root, text="", fg='white', bg='#1f1f1f', font=('Georgia', 12))
    login_msg.pack()
    
    Button(root, text='Log In', bg='#27ae60', fg='white', width=30, height=1, font=('Georgia', 14, 'bold'), relief=FLAT, command=validate_login).pack(pady=10)
    Button(root, text='Sign Up', bg='#2980b9', fg='white', width=30, height=1, font=('Georgia', 14, 'bold'), relief=FLAT, command=open_signup).pack(pady=10)
    
    root.mainloop()

main_screen()