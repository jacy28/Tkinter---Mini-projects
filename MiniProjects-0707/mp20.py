# ✅ 20. Calculator GUI
# Scenario: Create a calculator for basic arithmetic operations.
# Features:
# •	Entry fields for number inputs.
# •	Combobox to select operator.
# •	Button to calculate result.
# •	Error handling (e.g., division by zero).
# •	Result in Label.

import tkinter as tk
from tkinter import ttk, messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operator = operator_box.get()

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2
        else:
            result = "Invalid operator"

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Cannot divide by zero.")
        result_label.config(text="Result: Error")

root = tk.Tk()
root.title("Calculator")
root.geometry("300x250")

tk.Label(root, text="Number 1:").pack(pady=(10, 0))
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Number 2:").pack(pady=(10, 0))
entry2 = tk.Entry(root)
entry2.pack()

tk.Label(root, text="Operator:").pack(pady=(10, 0))
operator_box = ttk.Combobox(root, values=["+", "-", "*", "/"], state="readonly")
operator_box.pack()
operator_box.set("+")

tk.Button(root, text="Calculate", command=calculate).pack(pady=15)

result_label = tk.Label(root, text="Result:", font=("Arial", 12))
result_label.pack()

root.mainloop()
