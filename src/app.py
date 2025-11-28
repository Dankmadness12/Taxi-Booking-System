import tkinter as tk

root = tk.Tk()

# Creating the window
root.title("Welcome to Taxi Bookings Inc.")
root.geometry("200x80")
root.configure(background="white")
root.minsize(500, 400)
root.maxsize(1000, 500)
root.geometry("300x300+50+50")

tk.Label(root, text="Taxi Bookings Inc.", font=("Helvetica", 30), anchor="center").pack()

#BUTTON <-------

def on_click():
    label.config(text="Redirecting...")

button = tk.Button(
    root,
    text="Book a Taxi",
    command=on_click,
)

# A helper label to show the result of the click
label = tk.Label(root, text="...")
label.pack(padx=30, pady=30)


root.mainloop()
