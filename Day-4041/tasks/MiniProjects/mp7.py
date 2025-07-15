# 🔐 7. Password Strength Checker
# Goal: Check if entered password is strong.
# Requirements:
# •	Use Entry for password input (show="*").
# •	Use regex to check for uppercase, lowercase, number, symbol.
# •	Show strength feedback using Label.
# •	Layout with pack() or grid().

import tkinter as tk
import re

# --- Password strength checking logic ---
def check_strength():
    password = password_entry.get()

    # Conditions
    length_ok = len(password) >= 8
    has_upper = re.search(r"[A-Z]", password)
    has_lower = re.search(r"[a-z]", password)
    has_digit = re.search(r"\d", password)
    has_symbol = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    # Strength evaluation
    if not password:
        strength_label.config(text="Please enter a password", fg="red")
    elif all([length_ok, has_upper, has_lower, has_digit, has_symbol]):
        strength_label.config(text="Strong Password ✅", fg="green")
    elif length_ok and (has_upper and has_lower) and (has_digit or has_symbol):
        strength_label.config(text="Medium Password ⚠️", fg="orange")
    else:
        strength_label.config(text="Weak Password ❌", fg="red")

# --- GUI setup ---
root = tk.Tk()
root.title("🔐 Password Strength Checker")
root.geometry("400x200")

# --- Widgets ---
tk.Label(root, text="Enter Password:", font=("Arial", 12)).pack(pady=10)

password_entry = tk.Entry(root, show="*", font=("Arial", 12), width=30)
password_entry.pack()

check_btn = tk.Button(root, text="Check Strength", command=check_strength)
check_btn.pack(pady=10)

strength_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
strength_label.pack(pady=10)

root.mainloop()
