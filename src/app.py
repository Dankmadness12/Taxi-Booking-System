from pydoc import pager
import tkinter as tk
from tkinter import ttk
from typing import Self
import login
import register

root = tk.Tk()

# Landing Page <-------
class Homepage(tk.Tk):
    def __init__(self):
        super().__init__()
root.title("Welcome to Taxi Bookings Inc.")
root.geometry("500x400")
root.minsize(500, 400)
root.maxsize(1000, 500)

#Container Frame
container = tk.Frame(root)
container.pack(side="top", fill="both", expand=True)

root.frames = {}

tk.Label(root, text="Taxi Bookings Inc.", font=("Helvetica", 30), anchor="center").pack()

#Homepage Buttons <-------
login = tk.Button(root, text="Login", font=("Helvetica", 18), bg="blue", fg="white")
login.pack(padx=20, pady=25)

register = tk.Button(root, text="Register", font=("Helvetica", 18), bg="yellow", fg="black")
register.pack(padx=20, pady=25)

register = tk.Button(root, text="Exit", font=("Helvetica", 15), bg="green", fg="black", command=root.quit)
register.pack(padx=20, pady=25)

for F in (Homepage, login, register):
    frame = F()
    root.frames[F] = frame
    pager.name = F.__name__
    frame=F(parent=container, controller=root)
    frame.grid(row=0, column=0, sticky="nsew")

    root.show_frame = Homepage

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class Login(tk.Tk):
    def __init__(self) -> Self:
        super().__init__()
        label = tk.Label(self, text="Login Page", font=("Helvetica", 24))
        label.pack(pady=20)

root.mainloop()
