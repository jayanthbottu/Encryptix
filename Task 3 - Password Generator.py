import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Password length must be a positive integer")
        
        # Define the character set
        characters = string.ascii_letters + string.digits + string.punctuation
        
        # Generate the password
        password = ''.join(random.choice(characters) for _ in range(length))
        
        # Display the password
        password_display.config(text=password)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def copy_to_clipboard():
    password = password_display.cget("text")
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Success", "Password copied to clipboard")
    else:
        messagebox.showerror("Error", "No password generated")

# Create main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x350")
root.resizable(False, False)

# Create and place widgets
tk.Label(root, text="Enter desired password length:").pack(pady=10)
length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=20)

password_display = tk.Label(root, text="", wraplength=380, font=("Courier", 12))
password_display.pack(pady=10)

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=10)

root.mainloop()