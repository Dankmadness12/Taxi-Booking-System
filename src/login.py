import tkinter as tk
from tkinter import ttk

def open_login_window():
    login_window = tk.Toplevel()
    login_window.title("Login")
    login_window.geometry("300x200")
    
    tk.Label(login_window, text="Username:", font=("Helvetica", 14)).pack(pady=10)
    username_entry = tk.Entry(login_window, font=("Helvetica", 14))
    username_entry.pack(pady=5)
    
    tk.Label(login_window, text="Password:", font=("Helvetica", 14)).pack(pady=10)
    password_entry = tk.Entry(login_window, show="*", font=("Helvetica", 14))
    password_entry.pack(pady=5)
    
    login_button = tk.Button(login_window, text="Submit", font=("Helvetica", 14), bg="blue", fg="white")
    login_button.pack(pady=20)