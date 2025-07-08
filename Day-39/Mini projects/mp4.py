# 4.	Unit Converter
# Convert between centimeters/inches, celsius/fahrenheit, etc., with Entry fields for input and output.

import tkinter as tk
from tkinter import ttk, messagebox

root=tk.Tk()
root.title("Unit Converter")
root.geometry("300x300")

def convert():
    try:
        value = float(input_entry.get())
        conversion = conversion_combobox.get()

        if conversion == "cm to inch":
            result = value / 2.54
        elif conversion == "inch to cm":
            result = value * 2.54
        elif conversion == "Celsius to Fahrenheit":
            result = (value * 9/5) + 32
        elif conversion == "Fahrenheit to Celsius":
            result = (value - 32) * 5/9
        else:
            result_output.delete(0, tk.END)
            result_output.insert(0, "Select a valid conversion")
            return

        result_output.delete(0, tk.END)
        result_output.insert(0, f"{round(result, 2)}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a numeric value.")

tk.Label(root, text="Enter Value:").pack(pady=5)
input_entry = tk.Entry(root, font=("Arial", 12), width=20)
input_entry.pack(pady=5)

tk.Label(root, text="Select Conversion:").pack(pady=5)
conversion_combobox = ttk.Combobox(root, values=[
    "cm to inch", "inch to cm", 
    "Celsius to Fahrenheit", "Fahrenheit to Celsius"
], state="readonly", width=30)
conversion_combobox.pack()
conversion_combobox.set("cm to inch")

tk.Button(root, text="Convert", command=convert, bg="lightblue", width=20).pack(pady=10)

tk.Label(root, text="Result:").pack(pady=5)
result_output = tk.Entry(root, font=("Arial", 12), width=20, state="normal")
result_output.pack(pady=5)

root.mainloop()

