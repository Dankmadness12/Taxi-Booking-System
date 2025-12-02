import tkinter as tk
from tkinter import ttk

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
        ttk.Label(self, text="Welcome", font=("Helvetica", 22)).pack(pady=30)
        ttk.Button(self, text="Login", command=lambda: controller.show_frame("LoginPage")).pack(pady=10)
        ttk.Button(self, text="Register", command=lambda: controller.show_frame("RegisterPage")).pack(pady=10)
        ttk.Button(self, text="Exit", command=controller.destroy).pack(pady=20)

#The Login Page <-------------------------------------------------
class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        ttk.Label(self, text="Login Page", font=("Helvetica", 18)).pack(pady=20)
        ttk.Entry(self).pack()
        ttk.Button(self, text="Back", command=lambda: controller.show_frame("Homepage")).pack(pady=10)

#The Register Page <-------------------------------------------------
class RegisterPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        ttk.Label(self, text="Register Page", font=("Helvetica", 18)).pack(pady=20)
        ttk.Entry(self).pack()
        ttk.Button(self, text="Back", command=lambda: controller.show_frame("Homepage")).pack(pady=10)

if __name__ == "__main__":
    app = TaxiBookings()
    app.mainloop()
