# 49. Unit Converter with History
# •	Convert between units: length, mass, temp, etc.
# •	Log all conversions with timestamp
# •	Search history
# •	Save/load preferences
# •	Add custom units

import tkinter as tk
from tkinter import ttk, messagebox
import time
import json
import pandas as pd

# === Conversion logic ===
unit_categories = {
    "Length": {
        "m": 1,
        "km": 1000,
        "cm": 0.01,
        "mm": 0.001,
        "ft": 0.3048,
        "in": 0.0254,
        "mi": 1609.34
    },
    "Mass": {
        "kg": 1,
        "g": 0.001,
        "lb": 0.453592,
        "oz": 0.0283495
    },
    "Temperature": {
        "C": "C",
        "F": "F",
        "K": "K"
    }
}

history = []

# === Functions ===
def convert():
    try:
        category = category_cb.get()
        val = float(value_var.get())
        from_unit = from_cb.get()
        to_unit = to_cb.get()

        if category == "Temperature":
            result = convert_temp(val, from_unit, to_unit)
        else:
            base = unit_categories[category][from_unit]
            target = unit_categories[category][to_unit]
            result = val * base / target

        result_var.set(f"{result:.4f}")
        log_conversion(val, from_unit, to_unit, result)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def convert_temp(val, from_u, to_u):
    if from_u == to_u:
        return val
    if from_u == "C":
        return val * 9/5 + 32 if to_u == "F" else val + 273.15
    elif from_u == "F":
        return (val - 32) * 5/9 if to_u == "C" else (val - 32) * 5/9 + 273.15
    elif from_u == "K":
        return val - 273.15 if to_u == "C" else (val - 273.15) * 9/5 + 32

def log_conversion(val, from_u, to_u, result):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    entry = f"{timestamp} | {val} {from_u} → {result:.4f} {to_u}"
    history.append(entry)
    history_list.insert(tk.END, entry)

def update_units(event=None):
    category = category_cb.get()
    if category not in unit_categories:
        return
    units = list(unit_categories[category].keys())
    from_cb['values'] = units
    to_cb['values'] = units
    from_cb.set(units[0])
    to_cb.set(units[1] if len(units) > 1 else units[0])

def search_history():
    query = search_var.get().lower()
    history_list.delete(0, tk.END)
    for item in history:
        if query in item.lower():
            history_list.insert(tk.END, item)

def export_history():
    df = pd.DataFrame(history, columns=["Log"])
    df.to_csv("conversion_history.csv", index=False)
    messagebox.showinfo("Exported", "History saved to CSV.")

def save_preferences():
    prefs = {
        "category": category_cb.get(),
        "from": from_cb.get(),
        "to": to_cb.get()
    }
    with open("prefs.json", "w") as f:
        json.dump(prefs, f)

def load_preferences():
    try:
        with open("prefs.json", "r") as f:
            prefs = json.load(f)
        category_cb.set(prefs.get("category", "Length"))
        update_units()
        from_cb.set(prefs.get("from", "m"))
        to_cb.set(prefs.get("to", "km"))
    except:
        # Set default if preferences not found
        category_cb.set("Length")
        update_units()

# === GUI ===
root = tk.Tk()
root.title("Unit Converter with History")
root.geometry("600x500")

value_var = tk.StringVar()
result_var = tk.StringVar()
search_var = tk.StringVar()

tk.Label(root, text="Enter value:").pack()
tk.Entry(root, textvariable=value_var).pack()

category_cb = ttk.Combobox(root, values=list(unit_categories.keys()), state="readonly")
category_cb.pack()
category_cb.bind("<<ComboboxSelected>>", update_units)

from_cb = ttk.Combobox(root, state="readonly")
from_cb.pack()

to_cb = ttk.Combobox(root, state="readonly")
to_cb.pack()

tk.Button(root, text="Convert", command=convert).pack(pady=10)
tk.Label(root, text="Result:").pack()
tk.Entry(root, textvariable=result_var, state="readonly").pack()

tk.Label(root, text="Search History:").pack()
tk.Entry(root, textvariable=search_var).pack()
tk.Button(root, text="Search", command=search_history).pack(pady=5)

history_list = tk.Listbox(root, height=10, width=80)
history_list.pack(pady=10)

tk.Button(root, text="Export History to CSV", command=export_history).pack()
tk.Button(root, text="Save Preferences", command=save_preferences).pack()

# Load user settings
category_cb.set("Length")  # default category
update_units()
load_preferences()

root.mainloop()
