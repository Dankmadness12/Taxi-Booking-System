import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# Landing Page <-------
class Homepage(tk.Tk):
    def __init__(self):
        super().__init__()
root.title("Welcome to Taxi Bookings Inc.")
root.geometry("500x400")
root.minsize(500, 400)
root.maxsize(1000, 500)

container = tk.Frame(root)
container.pack(side="top", fill="both", expand=True)

tk.Label(root, text="Taxi Bookings Inc.", font=("Helvetica", 30), anchor="center").pack()

#Homepage Buttons <-------
login = tk.Button(root, text="Login", font=("Helvetica", 18), bg="blue", fg="white")
login.pack(padx=20, pady=25)

register = tk.Button(root, text="Register", font=("Helvetica", 18), bg="yellow", fg="black")
register.pack(padx=20, pady=25)

register = tk.Button(root, text="Exit", font=("Helvetica", 15), bg="green", fg="black", command=root.quit)
register.pack(padx=20, pady=25)



root.mainloop()
