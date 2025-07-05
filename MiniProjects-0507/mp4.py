# 🟢 4. BMI Calculator
# Goal: Calculate BMI from height and weight inputs.
# Requirements:
# •	Use Entry or Spinbox for weight and height.
# •	Use Button to trigger BMI calculation.
# •	Show result with Label.config().
# •	Use grid() layout.
# •	Use input validation (numeric check).

import tkinter as tk

root = tk.Tk()
root.title("BMI Calculator")

def calculate_bmi():
    try:
        w = float(weight_entry.get())
        h = float(height_entry.get())
        if h <= 0 or w <= 0:
            result_var.set("Enter positive numbers.")
            return
        bmi = w / (h ** 2)
        result_var.set(f"BMI: {bmi:.2f}")
    except ValueError:
        result_var.set("Enter valid numbers.")

tk.Label(root, text="Weight (kg):").grid(row=0, column=0, padx=5, pady=5)
tk.Label(root, text="Height (m):").grid(row=1, column=0, padx=5, pady=5)

weight_entry = tk.Entry(root)
height_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1, padx=5, pady=5)
height_entry.grid(row=1, column=1, padx=5, pady=5)

calc_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calc_button.grid(row=2, column=0, columnspan=2, pady=10)

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var)
result_label.grid(row=3, column=0, columnspan=2)

root.mainloop()
