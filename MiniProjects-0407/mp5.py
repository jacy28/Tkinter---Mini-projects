# 5. Simple Calculator UI
# Objective: Perform basic arithmetic operations with Entry widgets.
# Features:
# •	Two Entry fields for numbers.
# •	Combobox for operation selection (+, -, *, /).
# •	Calculate on Button click.
# •	Result displayed via Label.
# •	Use grid() for aligning widgets.


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_combo.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2
        else:
            result_label.config(text="Select operation")
            return

        result_label.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Cannot divide by zero.")

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x200")

num1_label=tk.Label(root, text="Number 1:")
num1_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, pady=5)

num2_label=tk.Label(root, text="Number 2:")
num2_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, pady=5)

operation_label=tk.Label(root, text="Operation:")
operation_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
operation_combo = ttk.Combobox(root, values=["+", "-", "*", "/"], state="readonly", width=5)
operation_combo.grid(row=2, column=1, pady=5)
operation_combo.set("+")  

calc_button = tk.Button(root, text="Calculate", command=calculate)
calc_button.grid(row=3, columnspan=2, pady=10)

result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, columnspan=2, pady=5)

root.mainloop()
