import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def calculate(operation):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error: Division by Zero"
        else:
            result = "Invalid Operation"
        label_result.config(text=f"Result: {result}")
    except ValueError:
        label_result.config(text="Error: Invalid Input")

root = tk.Tk()
root.geometry("900x300")
root.title("Modern Calculator")

style = ttk.Style()
style.configure("TLabel", font=("Arial", 14))
style.configure("TButton", font=("Arial", 14))
style.configure("TEntry", font=("Arial", 14))

ttk.Label(root, text="Enter first number:").grid(row=0, column=0, padx=10, pady=10)
entry_num1 = ttk.Entry(root, width=30)
entry_num1.grid(row=0, column=1, padx=10, pady=10)

ttk.Label(root, text="Enter second number:").grid(row=1, column=0, padx=10, pady=10)
entry_num2 = ttk.Entry(root, width=30)
entry_num2.grid(row=1, column=1, padx=10, pady=10)

ttk.Label(root, text="Select operation:").grid(row=2, column=0, padx=10, pady=10)
frame_operations = ttk.Frame(root)
frame_operations.grid(row=2, column=1, padx=10, pady=10)

ttk.Button(frame_operations, text="+", command=lambda: calculate("+")).pack(side=tk.LEFT, padx=5)
ttk.Button(frame_operations, text="-", command=lambda: calculate("-")).pack(side=tk.LEFT, padx=5)
ttk.Button(frame_operations, text="*", command=lambda: calculate("*")).pack(side=tk.LEFT, padx=5)
ttk.Button(frame_operations, text="/", command=lambda: calculate("/")).pack(side=tk.LEFT, padx=5)

label_result = ttk.Label(root, text="Result: ")
label_result.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()