import tkinter as tk
from tkinter import ttk

root = tk.Tk()

#Creating the window
def open_login_window(parent=None):
    login_window = tk.Toplevel()
    login_window.title("Login")
    login_window.geometry("450x320")


    #The Username
    tk.Label(open_login_window, text="Username:", font=("Helvetica", 14)).pack(pady=10)
    label = tk.Entry(open_login_window, font=("Helvetica", 14))
    label.pack(pady=5 )
    
    #The Password
    tk.Label(open_login_window, text="Password:", font=("Helvetica", 14)).pack(pady=10)
    password_entry = tk.Entry(open_login_window, show="*", font=("Helvetica", 14))
    password_entry.pack(pady=5)
    
    #Submit Button
    login_button = tk.Button(open_login_window, text="Submit", font=("Helvetica", 14), bg="blue", fg="white")
    login_button.pack(pady=20)


    #Back Button
    back_button = tk.Button(open_login_window, text="Back", font=("Helvetica", 14), bg="gray", fg="black", command=open_login_window.destroy)
    back_button.pack(pady=10)


#Actually open the window (and mainloop I guess)
if __name__ == '__main__':
    root.withdraw()  
    open_login_window()
    root.mainloop()