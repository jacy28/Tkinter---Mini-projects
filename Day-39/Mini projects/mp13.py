# 13.	BMI Calculator
# 	Entries for height and weight, Button to calculate, and Label to show BMI result.

import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        height = float(height_entry.get())
        weight = float(weight_entry.get())

        if height <= 0 or weight <= 0:
            raise ValueError

        bmi = weight / ((height / 100) ** 2)  # Convert cm to meters
        result = f"Your BMI is: {bmi:.2f}"

        # Optional: add BMI category
        if bmi < 18.5:
            result += " (Underweight)"
        elif 18.5 <= bmi < 25:
            result += " (Normal)"
        elif 25 <= bmi < 30:
            result += " (Overweight)"
        else:
            result += " (Obese)"

        result_label.config(text=result)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values for height and weight.")

# Setup window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("350x250")

tk.Label(root, text="Height (cm):").grid(row=0, column=0, padx=10, pady=10, sticky="e")
height_entry = tk.Entry(root)
height_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Weight (kg):").grid(row=1, column=0, padx=10, pady=10, sticky="e")
weight_entry = tk.Entry(root)
weight_entry.grid(row=1, column=1, padx=10, pady=10)

# Button
tk.Button(root, text="Calculate BMI", command=calculate_bmi).grid(row=2, column=1, pady=15)

# Result
result_label = tk.Label(root, text="Your BMI will appear here")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()

