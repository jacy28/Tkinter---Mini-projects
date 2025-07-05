# 🟢 11. Temperature Converter App
# Goal: Convert Celsius ↔ Fahrenheit.
# Requirements:
# •	Spinbox to input temperature.
# •	Combobox to select "Celsius to Fahrenheit" or reverse.
# •	Show result in Label.
# •	Use Button to convert.
# •	Align using pack() or grid().

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Temperature Converter")

tk.Label(root, text="Temperature:").grid(row=0, column=0, padx=5, pady=5)

temp_spinbox = tk.Spinbox(root, from_=-100, to=100, width=10)
temp_spinbox.grid(row=0, column=1, padx=5, pady=5)

convert_choice = ttk.Combobox(root, values=["Celsius to Fahrenheit", "Fahrenheit to Celsius"])
convert_choice.set("Celsius to Fahrenheit")
convert_choice.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=("Arial", 12))
result_label.grid(row=3, column=0, columnspan=2, pady=10)

def convert_temp():
    try:
        temp = float(temp_spinbox.get())
        mode = convert_choice.get()
        if mode == "Celsius to Fahrenheit":
            result = (temp * 9/5) + 32
            result_var.set(f"{temp}°C = {result:.2f}°F")
        else:
            result = (temp - 32) * 5/9
            result_var.set(f"{temp}°F = {result:.2f}°C")
    except ValueError:
        result_var.set("Invalid input.")

convert_btn = tk.Button(root, text="Convert", command=convert_temp)
convert_btn.grid(row=2, column=0, columnspan=2, pady=5)

root.mainloop()

