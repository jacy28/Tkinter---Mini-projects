# ✅ 9. BMI Calculator
# Scenario: GUI for calculating Body Mass Index.
# Features:
# •	Entry or Spinbox for height and weight.
# •	Button to calculate and display BMI.
# •	Use .config() to update result in Label.

import tkinter as tk

def calculate_bmi():
    try:
        height_cm = float(height_spinbox.get())
        weight_kg = float(weight_spinbox.get())
        height_m = height_cm / 100
        bmi = weight_kg / (height_m ** 2)
        result_label.config(text=f"BMI: {bmi:.2f}")
    except:
        result_label.config(text="Invalid input", fg="red")

root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x250")

tk.Label(root, text="Height (cm):").pack(pady=(20, 5))
height_spinbox = tk.Spinbox(root, from_=50, to=250, width=10)
height_spinbox.pack()

tk.Label(root, text="Weight (kg):").pack(pady=(10, 5))
weight_spinbox = tk.Spinbox(root, from_=10, to=200, width=10)
weight_spinbox.pack()

tk.Button(root, text="Calculate BMI", command=calculate_bmi).pack(pady=20)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

root.mainloop()
