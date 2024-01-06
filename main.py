# Import Tkinter and modules
import tkinter as tk
from tkinter import Button

# Import custom Tkinter and modules
import customtkinter
from customtkinter import CTkButton
from customtkinter import CTkEntry

# Create the store passwords function
def store():
    with open ("Passwords.txt", "a") as passwrds:
        passwrds.write ("" + site.get() + " | " + password.get() + " \n") 
     
# Set the colour scheme
customtkinter.set_appearance_mode("system") # Colour is set to system so when it changes when the user changes there colour scheme
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()

# Set the windows size
root.geometry("400x320")

# Set the windows title
root.title("CryptoniteKeeper")

# Add a button
text = CTkButton(root, text = "Store", command = store, corner_radius=55)
text.pack (padx=10, pady=10)

# Add a textbox where user would input the site or service for the password
site = tk.StringVar()
service = CTkEntry(root, width=400, height=40, textvariable = site)
service.pack (padx=10, pady=10)

# Create the rextbox where the user will enter their password
password = tk.StringVar()
passwordbox = CTkEntry(root, width=400, height=40, textvariable = password)
passwordbox.pack (padx=10, pady=10)

# Create the mainloop to keep the app running
root.mainloop()