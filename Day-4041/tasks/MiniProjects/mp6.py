# 🧮 6. Simple Calculator
# Goal: Perform basic arithmetic operations.
# Requirements:
# •	Entry for input.
# •	Buttons for +, -, *, /, =, and C.
# •	Display result in Entry or Label.
# •	Use grid() layout.
# •	Validate for division by zero.

import tkinter as tk

def on_button_click(char):
    if char == '=':
        try:
            expression = entry.get()
            result = eval(expression)
            entry.delete(0, tk.END)
            entry.insert(0, str(result))
        except ZeroDivisionError:
            entry.delete(0, tk.END)
            entry.insert(0, "Error: Divide by 0")
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(0, "Invalid Input")
    elif char == 'C':
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, char)

# --- GUI Setup ---
root = tk.Tk()
root.title("🧮 Simple Calculator")
root.geometry("300x400")
root.resizable(False, False)

entry = tk.Entry(root, font=("Arial", 18), justify="right", bd=5, relief=tk.RIDGE)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="we")

# --- Button Layout ---
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0)
]

for (text, row, col) in buttons:
    btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                    command=lambda t=text: on_button_click(t))
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# Make last row span 4 columns for 'C' button
root.grid_rowconfigure(5, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()
