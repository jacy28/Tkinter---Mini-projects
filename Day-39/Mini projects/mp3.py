# 3.	Basic Calculator
# Use Entry widgets and Buttons for digits and operations (+, -, ×, ÷), displaying results in a Label.

import tkinter as tk

root = tk.Tk()
root.title("Basic Calculator")
root.geometry("300x400")

expression_entry = tk.Entry(root, font=("Arial", 18), borderwidth=2, relief="sunken", justify="right")
expression_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

result_label = tk.Label(root, text="", font=("Arial", 14), fg="green")
result_label.grid(row=1, column=0, columnspan=4)

def add_to_expression(char):
    expression_entry.insert(tk.END, char)

def clear_expression():
    expression_entry.delete(0, tk.END)
    result_label.config(text="")

def calculate():
    expr = expression_entry.get().replace("×", "*").replace("÷", "/")
    try:
        result = eval(expr)
        result_label.config(text=f"Result: {result}", fg="green")
    except Exception:
        result_label.config(text="Error!", fg="red")

buttons = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('÷', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('×', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('+', 5, 3),
]

for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, width=5, height=2, command=calculate)
    else:
        btn = tk.Button(root, text=text, width=5, height=2, command=lambda t=text: add_to_expression(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

clear_btn = tk.Button(root, text="Clear", width=22, height=2, bg="lightgray", command=clear_expression)
clear_btn.grid(row=6, column=0, columnspan=4, padx=10, pady=10)

root.mainloop() 

