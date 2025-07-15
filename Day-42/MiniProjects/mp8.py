# 🔷 8. Temperature Converter
# Widgets Used: Combobox, Spinbox, Button, Label
# Requirements:
# •	Input temperature via Spinbox.
# •	Choose unit (Celsius or Fahrenheit) via Combobox.
# •	Button to convert value to the other unit.
# •	Show result in Label.
# •	Allow dynamic update when Spinbox or Combobox changes.

import tkinter as tk
from tkinter import ttk

def convert_temperature(*args):
    try:
        temp = float(temp_spin.get())
        unit = unit_combo.get()
        if unit == "Celsius":
            converted = (temp * 9/5) + 32
            result_label.config(text=f"{converted:.2f} °F")
        elif unit == "Fahrenheit":
            converted = (temp - 32) * 5/9
            result_label.config(text=f"{converted:.2f} °C")
        else:
            result_label.config(text="Select Unit")
    except ValueError:
        result_label.config(text="Invalid input")

# --- Setup Window --- #
root = tk.Tk()
root.title("🔷 Temperature Converter")
root.geometry("350x250")

# --- Temperature Input --- #
tk.Label(root, text="Enter Temperature:").pack(pady=5)
temp_spin = tk.Spinbox(root, from_=-100, to=100, width=10, command=convert_temperature)
temp_spin.pack(pady=5)

# --- Unit Selection --- #
tk.Label(root, text="Select Unit:").pack(pady=5)
unit_combo = ttk.Combobox(root, values=["Celsius", "Fahrenheit"], state="readonly")
unit_combo.set("Celsius")
unit_combo.pack(pady=5)

# --- Convert Button --- #
tk.Button(root, text="Convert", command=convert_temperature).pack(pady=10)

# --- Result Label --- #
result_label = tk.Label(root, text="Result: ", font=("Arial", 14), fg="blue")
result_label.pack(pady=10)

# --- Dynamic Bindings --- #
unit_combo.bind("<<ComboboxSelected>>", convert_temperature)

root.mainloop()
