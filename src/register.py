import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# Creating the window
root.title("Register")
root.geometry("200x80")
root.minsize(500, 400)
root.maxsize(1000, 500)
root.geometry("300x300+50+50")

#Actually login
tk.Label(root, text="Register New User", font=("Helvetica", 30), anchor="center").pack()

#Enter your username
username_label = tk.Label(root, text="Username:", font=("Helvetica", 14))
username_label.pack(pady=10)
username_entry = tk.Entry(root, font=("Helvetica", 14))
username_entry.pack(pady=5)

#Enter your password
password_label = tk.Label(root, text="Password:", font=("Helvetica", 14))
password_label.pack(pady=10)
password_entry = tk.Entry(root, show="*", font=("Helvetica", 14))
password_entry.pack(pady=5)

#Register button
register_button = tk.Button(root, text="Register", font=("Helvetica", 14), bg="yellow", fg="black")
register_button.pack(pady=20)
root.mainloop()