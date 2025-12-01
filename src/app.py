import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# Creating the window
root.title("Welcome to Taxi Bookings Inc.")
root.geometry("200x80")
root.minsize(500, 400)
root.maxsize(1000, 500)
root.geometry("300x300+50+50")

tk.Label(root, text="Taxi Bookings Inc.", font=("Helvetica", 30), anchor="center").pack()
#BUTTON <-------

login = tk.Button(root, text="Login", font=("Helvetica", 18), bg="blue", fg="white")
login.pack(padx=20, pady=25)

register = tk.Button(root, text="Register", font=("Helvetica", 18), bg="yellow", fg="black")
register.pack(padx=20, pady=25)

register = tk.Button(root, text="Exit", font=("Helvetica", 15), bg="green", fg="black", command=root.quit)
register.pack(padx=20, pady=25)

root.mainloop()
