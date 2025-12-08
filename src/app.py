from cmath import e
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
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
        
        #All of the Frames <-------------------------------------------------
        self.frames = {}
        for Page in (Homepage, LoginPage, RegisterPage, Passenger, DriverLoginPage, Driver, AdminLoginPage, Admin, Bookings, Booking_Display):
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
        ttk.Button(self, text="Login as User", command=lambda: controller.show_frame("LoginPage")).pack(pady=20)
        ttk.Button(self, text="Login as Driver", command=lambda: controller.show_frame("DriverLoginPage")).pack(pady=20)
        ttk.Button(self, text="Login as Admin", command=lambda: controller.show_frame("AdminLoginPage")).pack(pady=20)
        ttk.Button(self, text="Register", command=lambda: controller.show_frame("RegisterPage")).pack(pady=20)
        ttk.Button(self, text="Exit", command=controller.destroy).pack(pady=20)

#The Login Page <-------------------------------------------------
class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        # store controller for use in callbacks
        self.controller = controller

        tk.Label(self, text="Login", font=("Helvetica", 20)).pack(pady=20)

        tk.Label(self, text="Username or Email").pack()
        self.username_entry = ttk.Entry(self)
        self.username_entry.pack()

        tk.Label(self, text="Password").pack(pady=10)
        self.password_entry = ttk.Entry(self, show="*")
        self.password_entry.pack(pady=5)

        ttk.Button(self, text="Login", command=self.login_user).pack(pady=15)
        ttk.Button(self, text="Back", command=lambda: controller.show_frame("Homepage")).pack(pady=10)
    
    #User Login Logic <-------------------------------------------------
    def login_user(self):
        identifier = self.username_entry.get().strip()
        password = self.password_entry.get()

        if not identifier or not password:
            messagebox.showerror("Error", "Please enter username/email and password.")
            return

        # hash password the same way as registration
        hashed_pw = hashlib.sha256(password.encode('utf-8')).hexdigest()

        try:
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute("SELECT user_id, password, username, email FROM Users WHERE username=? OR email=?", (identifier, identifier))
            row = cursor.fetchone()
            conn.close()

            if row is None:
                messagebox.showerror("Login Failed", "User not found, please register.")
                return

            user_id = row[0]
            stored_password = row[1]
            username = row[2]
            email = row[3]

            if stored_password == hashed_pw:
                # Store user info on controller
                self.controller.current_user_id = user_id
                self.controller.current_username = {"id": user_id, "username": username, "email": email}

                # Load passenger data if the frame has that method
                passengers_frame = self.controller.frames.get("Passenger")
                if passengers_frame and hasattr(passengers_frame, "load_passenger"):
                    passengers_frame.load_passenger(user_id)

                messagebox.showinfo("Login Success", f"Welcome back {username}!")
                self.controller.show_frame("Passenger")
                # Clear login fields
                self.username_entry.delete(0, tk.END)
                self.password_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Login Failed", "Incorrect password.")

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Database error during login: {e}")

#The Driver Login Page <-------------------------------------------------
class DriverLoginPage(tk.Frame): 
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        ttk.Label(self, text="Driver Login", font=("Helvetica", 18)).pack(pady=20)

        tk.Label(self, text="Username or Email").pack()
        self.username_entry = ttk.Entry(self)
        self.username_entry.pack()

        tk.Label(self, text="License Number").pack(pady=10)
        self.license_entry = ttk.Entry(self)
        self.license_entry.pack(pady=5)

        tk.Label(self, text="Password").pack(pady=10)
        self.password_entry = ttk.Entry(self, show="*")
        self.password_entry.pack(pady=5)

        ttk.Button(self, text="Login", command=self.login_driver).pack(pady=15)
        ttk.Button(self, text="Back", command=lambda: controller.show_frame("Homepage")).pack(pady=10)

    #Driver Login Logic <-------------------------------------------------------------
    def login_driver(self):
        identifier = self.username_entry.get().strip()
        license_number = self.license_entry.get()
        password = self.password_entry.get()

        if not identifier or not password:
            messagebox.showerror("Error", "Please enter username/password and license number.")
            return

        try:
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute("SELECT driver_id, name, email, password, phone_number, license_number, vehicle_details FROM Drivers WHERE name=? OR email=? OR license_number=?", (identifier, identifier, identifier))
            row = cursor.fetchone()
            conn.close()

            if row is None:
                messagebox.showerror("Login Failed", "Driver not found, please check your credentials.")
                return

            driver_id = row[0]
            name = row[1]
            email = row[2]
            stored_password = row[3]
            phone_number = row[4]
            license_number = row[5]
            vehicle_details = row[6]
            

            if stored_password == password:
                # Store user info on controller
                self.controller.current_driver_id = driver_id
                self.controller.current_username = {"id": driver_id, "username": name, "email": email, "password": password, "phone number": phone_number, "license number": license_number, "vehicle details": vehicle_details}
                
                # Load the driver data if the frame has that method
                if stored_password == password and license_number == license_number:
                    
                    self.controller.current_driver_id = driver_id
                    self.controller.current_username = {"id": driver_id, "username": name, "email": email, "license number": license_number, "password": password}
                    
                messagebox.showinfo("Login Success", f"Welcome back {name}!")
                self.controller.show_frame("Driver")
                # Clear login fields
                self.username_entry.delete(0, tk.END)
                self.password_entry.delete(0, tk.END)
                self.license_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Login Failed", "Incorrect credentials.")

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Database error during login: {e}")

#The Admin Login Page <-------------------------------------------------
class AdminLoginPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        ttk.Label(self, text="Admin Login", font=("Helvetica", 18)).pack(pady=20)

        tk.Label(self, text="Admin Username").pack()
        self.username_entry = ttk.Entry(self)
        self.username_entry.pack()
        
        ttk.Label(self, text="Admin Email").pack()
        self.email_entry = ttk.Entry(self)
        self.email_entry.pack()

        tk.Label(self, text="Password").pack(pady=10)
        self.password_entry = ttk.Entry(self, show="*")
        self.password_entry.pack(pady=5)

        ttk.Button(self, text="Login", command=self.login_admin).pack(pady=15)
        ttk.Button(self, text="Back", command=lambda: controller.show_frame("Homepage")).pack(pady=10)
    
    
    #The ADMIN Login Logic <---------------------------------------------------------------------------------
    def login_admin(self):
       identifier = self.username_entry.get().strip()
       password = self.password_entry.get()

       if not identifier or not password:
            messagebox.showerror("Error", "Please enter username/email and password.")
            return

       try:
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute("SELECT admin_id, username, email, password FROM Admin WHERE username=? OR email=? OR password=?", (identifier, identifier, identifier))
            row = cursor.fetchone()
            conn.close()

            if row is None:
                messagebox.showerror("Login Failed", "Invalid Admin Credentials, Try Again")
                return

            admin_id = row[0]
            username = row[1]
            email = row[2]
            stored_password = row[3]

            if stored_password == password:
                # Store user info on controller
                self.controller.current_user_id = admin_id
                self.controller.current_username = {"id": admin_id, "username": username, "email": email}

                # Load passenger data if the frame has that method
                admin_frame = self.controller.frames.get("Admin")
                if admin_frame and hasattr(admin_frame, "load_admin"):
                    admin_frame.load_passenger(admin_id)

                messagebox.showinfo("Login Success", f"Welcome home {username}!")
                self.controller.show_frame("Admin")
                # Clear login fields
                self.username_entry.delete(0, tk.END)
                self.email_entry.delete(0, tk.END)
                self.password_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Login Failed", "Incorrect Admin Password.")

       except sqlite3.Error as e:
         messagebox.showerror("Error", f"Database error during login: {e}")
        

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
    
    #Register User Function <-------------------------------------------------
    def register_user(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get()
        phone = self.phone_entry.get().strip()
        dob = self.dob_entry.get().strip()
        email = self.email_entry.get().strip()
        address = self.address_entry.get().strip()
        
        #Error message for the empty fields <-------------------------------------------------
        if not username or not password or not email:
            messagebox.showerror("Error", "Username, Password, and Email are required.")
            return
        
        #Hash the password <-------------------------------------------------
        hashed_pw = hashlib.sha256(password.encode('utf-8')).hexdigest()
        
        #Actually register as a user <-------------------------------------------------
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
            
            
           
           
                                           #--------------------------------> THE FRAMES <----------------------------------------------------
            
            

#The Passenger Frame <-------------------------------------------------
class Passenger(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        ttk.Label(self, text="Your Page", font=("Helvetica", 18)).pack(pady=20)
        ttk.Button(self, text="Book a Taxi", command=lambda: controller.show_frame("Bookings")).pack(pady=10)
        ttk.Button(self, text="View Your Bookings").pack(pady=10)
        ttk.Button(self, text="Logout", command=lambda: controller.show_frame("Homepage")).pack(pady=10)

#The Driver Frame <-------------------------------------------------
class Driver(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        ttk.Label(self, text="Driver's Page", font=("Helvetica", 18)).pack(pady=20)
        ttk.Button(self, text="View Bookings").pack(pady=10)
        ttk.Button(self, text="Assigned Trips").pack(pady=10)
        ttk.Button(self, text="Logout", command=lambda: controller.show_frame("Homepage")).pack(pady=10)

#The Admin Frame <-------------------------------------------------
class Admin(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        ttk.Label(self, text="Welcome Home, Admin", font=("Helvetica", 18)).pack(pady=20)
        ttk.Button(self, text="Assign Driver to Bookings").pack(pady=10)
        ttk.Button(self, text="Logout", command=lambda: controller.show_frame("Homepage")).pack(pady=10)
        
#The Bookings Frame <-------------------------------------------------
class Bookings(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        ttk.Label(self, text="Book Your Booking (HAH) Today!", font=("Helvetica", 18)).pack(pady=20)
        
        #Choose a Date <--------------------------------------------------------
        ttk.Label(self, text="Choose a Date").pack(pady=10)
        self.date_entry = DateEntry(self, width=10)
        self.date_entry.pack(pady=5)
        
        #Choose the pickup time <-------------------------------------------------
        ttk.Label(self, text="Choose a pickup time").pack()
        time = []
        for hour in range(0, 24):
            time.append(f"{hour:02d}:00")
            time.append(f"{hour:02d}:30")
        self.pickup_time_entry = ttk.Combobox(self, values=time, state='readonly')
        self.pickup_time_entry.pack(pady=10)
                
        #Choose the pickup location <-----------------------------------------------------
        ttk.Label(self, text="Choose a pickup location").pack()
        self.pickup_location_entry = ttk.Combobox(self, values=["Port-of-Spain", "Chaguanas", "Couva", "Freeport", "Carapichaima", "Chase Village", "Arima", "San Fernando"], state='readonly')
        self.pickup_location_entry.pack(pady=10)
        
        #Choose a dropoff location <-------------------------------------------------------
        ttk.Label(self, text="Choose a dropoff location").pack()
        self.dropoff_location_entry = ttk.Combobox(self, values=["Port-of-Spain", "Chaguanas", "Couva", "Freeport", "Carapichaima", "Chase Village", "Arima", "San Fernando"], state='readonly')
        self.dropoff_location_entry.pack(pady=10)
        
        ttk.Button(self, text="Book a Taxi", command=self.make_bookings).pack(pady=10)
        
        ttk.Button(self, text="Back", command=lambda: controller.show_frame("Passenger")).pack(pady=10)
        
    #Bookings Page Logic <------------------------------------------------------------------------------------
    def make_bookings(self):
        date = self.date_entry.get().strip()
        pickup_time = self.pickup_time_entry.get().strip()
        pickup_location = self.pickup_location_entry.get().strip()
        dropoff_location = self.dropoff_location_entry.get().strip()
            
        #Validation Checks and stuff    
        if pickup_location.lower() == dropoff_location.lower():
            messagebox.showerror("Invalid", "Please choose a seperate pickup and dropoff location")
            return
        
        if not date:
            messagebox.showerror("Error", "Please Enter a Date")
            return
        
        if not pickup_time:
            messagebox.showerror("Error", "Please select a time")
            return
        
        if not pickup_location or not dropoff_location:
            messagebox.showerror("Error", "Please enter your desired pickup/dropoff locations")
            return
        
        try:
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute("""INSERT INTO Bookings_Display (user_id, date, time, pickup_location, dropoff_location) 
                        VALUES (?, ?, ?, ?, ?)""", (self.controller.current_user_id, date, pickup_time, pickup_location, dropoff_location))
            conn.commit()
            conn.close()
            
            #The Message that the bookings was a success! And the display frame to......display the frame <-----------------------------------
            messagebox.showinfo("Success", "Booking Created Successfully!")
            display_frame = self.controller.frames["Booking_Display"]
            display_frame.load_bookings()
            self.controller.show_frame("Booking_Display")
            
        except sqlite3.Error as e:
          messagebox.showerror("Database error", str(e))
        
        
        
class Booking_Display(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        ttk.Label(self, text="Created Bookings", font=("Helvetica", 18)).pack(pady=20)
        
        #The Table to Display the Bookings made <---------------------------------------------------------
        table = ttk.Treeview(self)
        table.pack(fill='both', expand=True)
        
        #Naming the Columns <-------------------------------------------------------------
        table['columns']=('Date', 'Time', 'Pickup Location', 'Dropoff Location')
        table['show'] = 'headings'
        
        #Column Format (How's your day going?) <----------------------------------------------------
        table.column('Date', anchor=tk.W, width=110)
        table.column('Time', anchor=tk.W, width=100)
        table.column('Pickup Location', anchor=tk.W, width=150)
        table.column('Dropoff Location', anchor=tk.W, width=150)
        
        #The Table Headings <-------------------------------------------------------------------------
        table.heading('Date', text='Date', anchor=tk.W)
        table.heading('Time', text='Time', anchor=tk.W)
        table.heading('Pickup Location', text='Dropoff Location', anchor=tk.W)
        table.heading('Dropoff Location', text='Dropoff Location', anchor=tk.W)
        
        table.pack(expand=True, fill=tk.BOTH)
        
if __name__ == "__main__":
    app = TaxiBookings()
    app.mainloop()
