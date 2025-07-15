# 📆 13. Age Calculator
# Goal: Calculate age based on date of birth input.
# Requirements:
# •	Use Entry for DOB (YYYY-MM-DD).
# •	Validate format using regex.
# •	Calculate using datetime.
# •	Show result in Label.

import tkinter as tk
import re
from datetime import datetime

# --- Age Calculation Function ---
def calculate_age():
    dob = dob_entry.get()
    pattern = r"^\d{4}-\d{2}-\d{2}$"

    if not re.match(pattern, dob):
        result_label.config(text="❌ Invalid format. Use YYYY-MM-DD", fg="red")
        return

    try:
        birth_date = datetime.strptime(dob, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - birth_date.year

        # Adjust if birthday hasn’t occurred this year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1

        result_label.config(text=f"✅ You are {age} years old.", fg="green")
    except ValueError:
        result_label.config(text="❌ Invalid date entered.", fg="red")

# --- GUI Setup ---
root = tk.Tk()
root.title("📆 Age Calculator")
root.geometry("350x200")

# --- Widgets ---
tk.Label(root, text="Enter DOB (YYYY-MM-DD):", font=("Arial", 11)).pack(pady=10)
dob_entry = tk.Entry(root, font=("Arial", 12))
dob_entry.pack(pady=5)

tk.Button(root, text="Calculate Age", command=calculate_age).pack(pady=10)
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
