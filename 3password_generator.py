import random
import string
import tkinter as tk
from tkinter import ttk, messagebox

def generate_password(length, use_upper, use_lower, use_digits, use_punctuation):
    characters = ''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_punctuation:
        characters += string.punctuation

    if not characters:
        return "Select at least one character set!"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def on_generate():
    try:
        length = int(entry_length.get())
        use_upper = var_upper.get()
        use_lower = var_lower.get()
        use_digits = var_digits.get()
        use_punctuation = var_punctuation.get()

        if length <= 0:
            raise ValueError("Password length must be greater than 0.")
        
        password = generate_password(length, use_upper, use_lower, use_digits, use_punctuation)
        show_password_window(password)
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))

def show_password_window(password):
    new_window = tk.Toplevel(root)
    new_window.title("Generated Password")
    
    ttk.Label(new_window, text="Your Generated Password:", font=("Helvetica", 12, "bold")).pack(pady=10)
    entry_password = ttk.Entry(new_window, width=50)
    entry_password.pack(pady=10)
    entry_password.insert(0, password)
    
    ttk.Button(new_window, text="Close", command=new_window.destroy).pack(pady=10)

# Main application window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")

# Apply styles
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 10))
style.configure("TButton", font=("Helvetica", 10, "bold"))
style.configure("TCheckbutton", font=("Helvetica", 10))

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Widgets
ttk.Label(frame, text="Password Length:").grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
entry_length = ttk.Entry(frame, width=5)
entry_length.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

var_upper = tk.BooleanVar()
ttk.Checkbutton(frame, text="Include Uppercase Letters", variable=var_upper).grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

var_lower = tk.BooleanVar()
ttk.Checkbutton(frame, text="Include Lowercase Letters", variable=var_lower).grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

var_digits = tk.BooleanVar()
ttk.Checkbutton(frame, text="Include Digits", variable=var_digits).grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

var_punctuation = tk.BooleanVar()
ttk.Checkbutton(frame, text="Include Special Characters", variable=var_punctuation).grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

ttk.Button(frame, text="Generate Password", command=on_generate).grid(row=5, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
