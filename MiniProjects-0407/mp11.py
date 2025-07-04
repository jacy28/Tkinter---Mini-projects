# 11. Temperature Converter
# Objective: Convert between Celsius and Fahrenheit.
# Features:
# •	Spinbox for input temperature.
# •	Combobox to choose conversion direction.
# •	Button to perform conversion.
# •	Result displayed in Label.

import tkinter as tk
from tkinter import ttk

def convert_temperature():
    try:
        temp = float(temp_spinbox.get())
        direction = conversion_combo.get()

        if direction == "Celsius to Fahrenheit":
            result = (temp * 9/5) + 32
            result_label.config(text=f"{temp}°C = {result:.2f}°F")
        elif direction == "Fahrenheit to Celsius":
            result = (temp - 32) * 5/9
            result_label.config(text=f"{temp}°F = {result:.2f}°C")
        else:
            result_label.config(text="Select conversion type.")
    except ValueError:
        result_label.config(text="Invalid temperature input.")

root = tk.Tk()
root.title("Temperature Converter")
root.geometry("300x200")

input_frame = tk.Frame(root)
input_frame.pack(pady=15)

tk.Label(input_frame, text="Enter Temperature:").pack()
temp_spinbox = tk.Spinbox(input_frame, from_=-100, to=100, width=10)
temp_spinbox.pack()

tk.Label(input_frame, text="Convert:").pack(pady=(10, 0))
conversion_combo = ttk.Combobox(input_frame, values=["Celsius to Fahrenheit", "Fahrenheit to Celsius"], state="readonly")
conversion_combo.pack()
conversion_combo.set("Celsius to Fahrenheit")

convert_button = tk.Button(root, text="Convert", command=convert_temperature)
convert_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=5)

root.mainloop()
