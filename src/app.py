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

turn_on = tk.Button(root, text="Login", font=("Helvetica", 18), bg="blue", fg="white")
turn_on.pack(padx=5, pady=50)

turn_on = tk.Button(root, text="Register", font=("Helvetica", 18), bg="yellow", fg="black",)
turn_on.pack(padx=5, pady=5)


root.mainloop()
