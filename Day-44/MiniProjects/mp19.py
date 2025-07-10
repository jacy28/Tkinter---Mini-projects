# ✅ 19. Form Submission Dialog Box
# Objective: Show custom dialog after form submission.
# Features:
# •	Form with Entry widgets.
# •	Submit button opens a custom Toplevel() dialog.
# •	Dialog shows form values and "Close" button.

import tkinter as tk

def submit():
    name = name_entry.get()
    email = email_entry.get()

    dialog = tk.Toplevel(root)
    dialog.title("Submitted Info")
    dialog.geometry("250x100")

    tk.Label(dialog, text=f"Name: {name}").pack()
    tk.Label(dialog, text=f"Email: {email}").pack()
    tk.Button(dialog, text="Close", command=dialog.destroy).pack(pady=5)

root = tk.Tk()
root.geometry("300x200")

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Email").pack()
email_entry = tk.Entry(root)
email_entry.pack()

tk.Button(root, text="Submit", command=submit).pack(pady=10)

root.mainloop()
