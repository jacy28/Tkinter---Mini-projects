# ✅ 12. Calculator UI with Keyboard Support
# Objective: Support both mouse and keyboard input for calculations.
# Features:
# •	Entry for number input.
# •	Buttons for operations.
# •	Use key bindings for numbers and +, -, *, /, =.

import tkinter as tk

def on_button_click(char):
    if char == "C":
        expression_var.set("")
    elif char == "=":
        calculate()
    else:
        expression_var.set(expression_var.get() + char)

def on_key_press(event):
    key = event.char
    if key in "0123456789+-*/":
        expression_var.set(expression_var.get() + key)
    elif event.keysym == "Return":
        calculate()
    elif event.keysym == "BackSpace":
        expression_var.set(expression_var.get()[:-1])

def calculate():
    try:
        result = str(eval(expression_var.get()))
        expression_var.set(result)
    except:
        expression_var.set("Error")

root = tk.Tk()
root.geometry("300x350")
root.title("Calculator")

expression_var = tk.StringVar()

entry = tk.Entry(root, textvariable=expression_var, font=("Arial", 18), justify="right")
entry.pack(fill="x", padx=10, pady=10)
entry.focus_set()

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", "C", "=", "+"]
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(pady=2)
    for char in row:
        btn = tk.Button(frame, text=char, width=5, height=2, font=("Arial", 14), command=lambda c=char: on_button_click(c))
        btn.pack(side="left", padx=2)

for key in "0123456789+-*/":
    root.bind(key, on_key_press)
root.bind("<Return>", on_key_press)
root.bind("<BackSpace>", on_key_press)

root.mainloop()
