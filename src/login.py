import tkinter as tk
from tkinter import ttk

root = tk.Tk()

def open_login_window():
    login_window = tk.Toplevel()
    login_window.title("Login")
    login_window.geometry("300x300")
    
    tk.Label(login_window, text="Username:", font=("Helvetica", 14)).pack(pady=10)
    label = tk.Entry(login_window, font=("Helvetica", 14))
    label.pack(pady=5 )
    
    tk.Label(login_window, text="Password:", font=("Helvetica", 14)).pack(pady=10)
    password_entry = tk.Entry(login_window, show="*", font=("Helvetica", 14))
    password_entry.pack(pady=5)
    
    login_button = tk.Button(login_window, text="Submit", font=("Helvetica", 14), bg="blue", fg="white")
    login_button.pack(pady=20)


if __name__ == '__main__':
    # Create a root window so Toplevel has a parent, then open login and run the loop
    root.withdraw()  # hide the root window
    open_login_window()
    root.mainloop()