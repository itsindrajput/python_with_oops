from enum import unique
from pickle import BINGET
from tkinter import *
from PIL import ImageTk, Image
import mysql.connector
from tkinter import messagebox


# Function to connect to MySQL and create database & table
def setup_database():
    try:
        # Connect to MySQL server (without selecting a database)
        conn = mysql.connector.connect(host="localhost", user="root", password="Rishabh@124")
        cursor = conn.cursor()

        # Create database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS college")
        cursor.execute("USE college")

        conn.commit()
        cursor.close()
        conn.close()

    except mysql.connector.Error as e:
        messagebox.showerror("Database Error", f"Error: {e}")

def connection():
    firstname1 = firstname.get()
    lastname1 = lastname.get()
    email1 = email.get()
    phone1 = phone.get()
    password1 = cnfPassword.get()

    if not firstname1 or not lastname1 or not email1 or not phone1 or not password1:
        messagebox.showwarning("Fill All Fields", "You have to fill all the entries")
        return

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Rishabh@124",
        database="college"
    )
    mycursor = conn.cursor()

    try:
        # Create table if not exists
        mycursor.execute("""CREATE TABLE IF NOT EXISTS student(
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    firstName VARCHAR(100) NOT NULL,
                    lastName VARCHAR(100) NOT NULL,
                    email VARCHAR(255) NOT NULL UNIQUE,
                    phone BIGINT NOT NULL UNIQUE,
                    password VARCHAR(255) NOT NULL
                )""")

        ins = "INSERT INTO student(firstName, lastName, email, phone, password) VALUES(%s, %s, %s, %s, %s)"
        val = (firstname1, lastname1, email1, phone1, password1)
        mycursor.execute(ins,val)

        conn.commit()
        messagebox.showinfo("Success", "User Registered Successfully!")

    except mysql.connector.Error as e:
        messagebox.showerror("Database Error", f"Error: {e}")

    finally:
        conn.cursor()
        conn.close()

def ui():
    global firstname, lastname, email, phone, cnfPassword

    signup = Tk()
    signup.iconbitmap('favicon.ico')
    signup.title('Sign Up @ Capsule Coder')
    signup.geometry('400x500')
    signup.configure(background='#1f1f1f')

    # Load Image
    img = Image.open('logo.jpeg')
    resized_img = img.resize((80, 80), Image.Resampling.LANCZOS)
    signup.img = ImageTk.PhotoImage(resized_img)  # Store image reference

    Label(signup, image=signup.img, bg='#ffffff').pack(pady=(35, 10))
    Label(signup, text="Signup For Capsule Coder", fg='white', bg='red',
          font=('cambria', 18)).pack(pady=2)

    # Create Frame for First and Last Name using Frame
    aframe = Frame(signup, bg='#1f1f1f')
    aframe.pack(pady=(20, 0))
    # First Name
    Label(aframe, text="First Name", fg='white', bg='#1f1f1f', font=('georgia', 14)).grid(row=0, column=0, padx=10,
                                                                                          pady=3)
    firstname = Entry(aframe, width=25)
    firstname.grid(row=1, column=0, padx=12, pady=(5, 15))

    # Last Name
    Label(aframe, text="Last Name", fg='white', bg='#1f1f1f', font=('georgia', 14)).grid(row=0, column=1,
                                                                                         padx=10, pady=3)
    lastname = Entry(aframe, width=25)
    lastname.grid(row=1, column=1, padx=12, pady=(5, 15))

    # Email Id
    Label(aframe, text="Email I'd", fg='white', bg="#1f1f1f", font=('georgia', 14)).grid(row=2, column=0,
                                                                                         padx=10, pady=3)
    email = Entry(aframe, width=25)
    email.grid(row=3, column=0, padx=12, pady=(5, 15))

    # Phone Number
    Label(aframe, text="Phone Number", fg='white', bg="#1f1f1f", font=('georgia', 14)).grid(row=2, column=1,
                                                                                            padx=10, pady=3)
    phone = Entry(aframe, width=25)
    phone.grid(row=3, column=1, padx=12, pady=(5, 15))

    # Enter Password
    Label(aframe, text="Enter Password", fg='white', bg="#1f1f1f", font=('georgia', 14)).grid(row=4, column=0,
                                                                                              padx=10, pady=3)
    enterPassword = Entry(aframe, width=25, show='*')
    enterPassword.grid(row=5, column=0, padx=12, pady=(5, 15))

    # Confirm Password
    Label(aframe, text="Confirm Password", fg='white', bg="#1f1f1f", font=('georgia', 14)).grid(row=4, column=1,
                                                                                                padx=10, pady=3)
    cnfPassword = Entry(aframe, width=25, show='*')
    cnfPassword.grid(row=5, column=1, padx=12, pady=(5, 15))

    Button(signup, text='Create Account', fg='black', bg='#4fa261', width=30, height=1, font=('georgia', 14),
           command=connection).pack(pady=(10, 0))

    signup.mainloop()

setup_database()
ui()





