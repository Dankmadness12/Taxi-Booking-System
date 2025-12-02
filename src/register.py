import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# Creating the window
def open_register_window():
    register_window = tk.Toplevel()
    register_window.title("Register")
    register_window.geometry("450x400")

    # The Username
    tk.Label(open_register_window, text="Username:", font=("Helvetica", 14)).pack(pady=10)
    username_entry = tk.Entry(open_register_window, font=("Helvetica", 14))
    username_entry.pack(pady=5)

    # The Password
    tk.Label(open_register_window, text="Password:", font=("Helvetica", 14)).pack(pady=10)
    password_entry = tk.Entry(open_register_window, show="*", font=("Helvetica", 14))
    password_entry.pack(pady=5)

    # Register Button
    register_button = tk.Button(open_register_window, text="Register", font=("Helvetica", 14), bg="yellow", fg="black")
    register_button.pack(pady=20)

    # Back Button
    back_button = tk.Button(open_register_window, text="Back", font=("Helvetica", 14), bg="gray", fg="black", command=open_register_window.destroy)
    back_button.pack(pady=10)
# Actually open the window (and mainloop I guess)
if __name__ == '__main__':
    root.withdraw()  
    open_register_window()
    root.mainloop()