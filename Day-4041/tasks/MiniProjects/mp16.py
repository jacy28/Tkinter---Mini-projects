# 🛑 16. Terms and Conditions Checkbox
# Goal: Disable Submit button until terms checkbox is checked.
# Requirements:
# •	Checkbutton to agree to terms.
# •	Entry fields for user info.
# •	Button becomes active only when checkbox is checked.
# •	Layout with grid().

import tkinter as tk

def toggle_submit():
    if agree_var.get():
        submit_btn.config(state="normal")
    else:
        submit_btn.config(state="disabled")

def submit():
    name = name_entry.get()
    email = email_entry.get()
    result_label.config(text=f"Submitted!\nName: {name}, Email: {email}", fg="green")

# Create main window
root = tk.Tk()
root.title("Terms & Conditions Form")
root.geometry("400x250")

# Name
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10)

# Email
tk.Label(root, text="Email:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
email_entry = tk.Entry(root)
email_entry.grid(row=1, column=1, padx=10, pady=10)

# Terms and Conditions
agree_var = tk.BooleanVar()
terms_check = tk.Checkbutton(root, text="I agree to the Terms and Conditions", variable=agree_var, command=toggle_submit)
terms_check.grid(row=2, column=0, columnspan=2, pady=10)

# Submit Button (disabled by default)
submit_btn = tk.Button(root, text="Submit", command=submit, state="disabled")
submit_btn.grid(row=3, column=0, columnspan=2, pady=10)

# Result Label
result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
