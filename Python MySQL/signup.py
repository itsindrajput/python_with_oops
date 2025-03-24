import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Function to connect to MySQL and create database & table
def setup_database():
    try:
        # Connect to MySQL server (without selecting a database)
        conn = mysql.connector.connect(host="localhost", user="root", password="Rishabh@124")
        cursor = conn.cursor()
        
        # Create database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")
        cursor.execute("USE mydatabase")
        
        # Create users table if it doesn't exist
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL
        )
        """)

        conn.commit()
        cursor.close()
        conn.close()
        
    except mysql.connector.Error as e:
        messagebox.showerror("Database Error", f"Error: {e}")

# Function to store user data in the database
def register_user():
    name = entry_name.get()
    email = entry_email.get()
    password = entry_password.get()

    if not name or not email or not password:
        messagebox.showerror("Error", "All fields are required!")
        return

    try:
        # Connect to MySQL database
        conn = mysql.connector.connect(host="localhost", user="root", password="Rishabh@124", database="mydatabase")
        cursor = conn.cursor()

        # Insert data into the users table
        query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
        values = (name, email, password)
        cursor.execute(query, values)
        conn.commit()

        messagebox.showinfo("Success", "User Registered Successfully!")

        # Clear fields after registration
        entry_name.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_password.delete(0, tk.END)

    except mysql.connector.Error as e:
        messagebox.showerror("Database Error", f"Error: {e}")

    finally:
        cursor.close()
        conn.close()

# Setup database and table before starting GUI
setup_database()

# GUI Setup
root = tk.Tk()
root.title("Signup Form")
root.geometry("300x250")

tk.Label(root, text="Signup Form", font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(root, text="Name:").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Email:").pack()
entry_email = tk.Entry(root)
entry_email.pack()

tk.Label(root, text="Password:").pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

tk.Button(root, text="Sign Up", command=register_user).pack(pady=10)

root.mainloop()
