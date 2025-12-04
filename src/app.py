import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import hashlib


#Order of Business: Edit this file to add more details to the Login and Register pages. <-------------------------------------------------

#Creating the main application <-------------------------------------------------
class TaxiBookings(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Taxi Bookings Inc.")
        self.geometry("700x500")
        
        #The container for the frames <-------------------------------------------------
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for Page in (Homepage, LoginPage, RegisterPage):
            name = Page.__name__
            frame = Page(parent=container, controller=self)
            self.frames[name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Homepage")

    def show_frame(self, page_name):
        self.frames[page_name].tkraise()

#The Landing Page <-------------------------------------------------
class Homepage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        ttk.Label(self, text="Welcome to TaxiBookings Inc.", font=("Helvetica", 22)).pack(pady=30)
        ttk.Button(self, text="Login", command=lambda: controller.show_frame("LoginPage")).pack(pady=20)
        ttk.Button(self, text="Register", command=lambda: controller.show_frame("RegisterPage")).pack(pady=20)
        ttk.Button(self, text="Exit", command=controller.destroy).pack(pady=20)

#The Login Page <-------------------------------------------------
class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        tk.Label(self, text="Login", font=("Helvetica", 20)).pack(pady=20) #<-------- Login Title
        tk.Label(self, text="Username").pack() #<-------- Username Label
        ttk.Entry(self).pack() #<-------- Username Entry
        tk.Label(self, text="Password").pack(pady=10) #<-------- Password Label
        ttk.Entry(self, text="Password", show="*").pack(pady=5) #<-------- Password Entry
        ttk.Button(self, text="Login").pack(pady=15) #<-------- Login Button
        ttk.Button(self, text="Back", command=lambda: controller.show_frame("Homepage")).pack(pady=10) #<-------- Back Button

#The Register Page <-------------------------------------------------
class RegisterPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        ttk.Label(self, text="Register", font=("Helvetica", 18)).pack(pady=20)

        tk.Label(self, text="Username").pack()
        self.username_entry = ttk.Entry(self)
        self.username_entry.pack()

        tk.Label(self, text="Password").pack(pady=7)
        self.password_entry = ttk.Entry(self, show="*")
        self.password_entry.pack(pady=7)

        tk.Label(self, text="Phone Number").pack()
        self.phone_entry = ttk.Entry(self)
        self.phone_entry.pack(pady=7)

        ttk.Label(self, text="Date of Birth (YYYY/MM/DD)").pack()
        self.dob_entry = ttk.Entry(self)
        self.dob_entry.pack(pady=7)

        tk.Label(self, text="Email").pack()
        self.email_entry = ttk.Entry(self)
        self.email_entry.pack(pady=7)

        tk.Label(self, text="Address").pack()
        self.address_entry = ttk.Entry(self)
        self.address_entry.pack(pady=7)

        ttk.Button(self, text="Register", command=self.register_user).pack(pady=7)
        ttk.Button(self, text="Back", command=lambda: controller.show_frame("Homepage")).pack(pady=10)

    def register_user(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get()
        phone = self.phone_entry.get().strip()
        dob = self.dob_entry.get().strip()
        email = self.email_entry.get().strip()
        address = self.address_entry.get().strip()

        if not username or not password or not email:
            messagebox.showerror("Error", "Username, Password, and Email are required.")
            return

        hashed_pw = hashlib.sha256(password.encode('utf-8')).hexdigest()

        try:
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO Users (username, email, password, date_of_birth, phone_number, address) VALUES (?, ?, ?, ?, ?, ?)",
                (username, email, hashed_pw, dob, phone, address)
            )
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "User registered successfully!")
            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
            self.dob_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)
            self.address_entry.delete(0, tk.END)
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "A user with that email already exists.")
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Failed to register user: {e}")


if __name__ == "__main__":
    app = TaxiBookings()
    app.mainloop()
