import tkinter as tk
from tkinter import ttk

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
        ttk.Label(self, text="Register", font=("Helvetica", 18)).pack(pady=20) #<-------- Register Title
        tk.Label(self, text="Username").pack() #<-------- Username Label
        ttk.Entry(self).pack() #<-------- Username Entry
        tk.Label(self, text="Password").pack(pady=7) #<-------- Password Label
        ttk.Entry(self, text="Password", show="*").pack(pady=7) #<-------- Password Entry
        tk.Label(self, text="Phone Number").pack() #<-------- Phone Number Label
        ttk.Entry(self, text="Phone Number").pack(pady=7) #<-------- Phone Number Entry
        ttk.Label(self, text="Date of Birth (DD/MM/YYYY)").pack() #<-------- DOB Label
        ttk.Entry(self, text="Date of Birth").pack(pady=7) #< -------- DOB Entry
        tk.Label(self, text="Email").pack() #<-------- Email Label
        ttk.Entry(self, text="Email").pack(pady=7) #<-------- Email Entry
        tk.Label(self, text="Address").pack() #<-------- Address Label
        ttk.Entry(self, text="Address").pack(pady=7) #<-------- Address Entry
        ttk.Button(self, text="Register").pack(pady=7) #<-------- Register Button
        ttk.Button(self, text="Back", command=lambda: controller.show_frame("Homepage")).pack(pady=10) #<-------- Back Button

if __name__ == "__main__":
    app = TaxiBookings()
    app.mainloop()
