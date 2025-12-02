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
label = tk.Label(root, text="Welcome to Taxi Bookings Inc.", font=("Helvetica", 24), anchor="center")
label.pack(pady=50)

#Buttons <-------

#Login
login_button = tk.Button(root, text="Login", font=("Helvetica", 18), bg="blue", fg="white", width=15, command=lambda: print("Login Clicked"))
login_button.pack(pady=20)

#Register
register_button = tk.Button(root, text="Register", font=("Helvetica", 18), bg="green", fg="white", width=15, command=lambda: print("Register Clicked"))
register_button.pack(pady=20)

#Exit
back_button = tk.Button(root, text="Exit", font=("Helvetica", 14), bg="gray", fg="black", command=root.destroy)
back_button.pack(pady=10)

#Container Frame
container = tk.Frame(root)
container.pack(side="top", fill="both", expand=True)


root.mainloop()
