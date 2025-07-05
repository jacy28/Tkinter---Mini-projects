# 🟢 13. Simple Calculator GUI
# Goal: GUI calculator for basic math.
# Requirements:
# •	Use Entry fields for inputs.
# •	Combobox to select operation (+, −, ×, ÷).
# •	Button to calculate and show result in Label.
# •	Handle divide-by-zero with error label.
# •	Organize using grid().

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Simple Calculator")

tk.Label(root, text="Number 1:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
tk.Label(root, text="Number 2:").grid(row=1, column=0, padx=5, pady=5, sticky="e")

entry1 = tk.Entry(root, width=15)
entry2 = tk.Entry(root, width=15)
entry1.grid(row=0, column=1, padx=5, pady=5)
entry2.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Operation:").grid(row=2, column=0, padx=5, pady=5, sticky="e")

operation_box = ttk.Combobox(root, values=["+", "-", "*", "/"], width=13)
operation_box.set("+")
operation_box.grid(row=2, column=1, padx=5, pady=5)

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=("Arial", 12), fg="blue")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_box.get()
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                result_var.set("Error: Divide by zero")
                return
            result = num1 / num2
        else:
            result_var.set("Invalid operation")
            return
        result_var.set(f"Result: {result:.2f}")
    except ValueError:
        result_var.set("Error: Invalid input")

calc_button = tk.Button(root, text="Calculate", command=calculate)
calc_button.grid(row=3, column=0, columnspan=2, pady=5)

root.mainloop()
