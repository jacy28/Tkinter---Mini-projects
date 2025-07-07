# ✅ 17. Travel Booking GUI
# Scenario: Book a travel package using dropdowns and entry fields.
# Features:
# •	Entry for name, email.
# •	Combobox for destination.
# •	Spinbox for number of travelers.
# •	Output confirmation with all data shown in a Label.

import tkinter as tk
from tkinter import ttk, messagebox

def confirm_booking():
    name = name_entry.get().strip()
    email = email_entry.get().strip()
    destination = destination_combo.get()
    travelers = travelers_spinbox.get()

    if not name or not email or not destination:
        messagebox.showerror("Missing Info", "Please fill all the fields.")
        return

    result = f"Booking Confirmed!\nName: {name}\nEmail: {email}\nDestination: {destination}\nTravelers: {travelers}"
    result_label.config(text=result)

root = tk.Tk()
root.title("Travel Booking")
root.geometry("400x350")

tk.Label(root, text="Name:").pack(anchor="w", padx=10, pady=(10, 0))
name_entry = tk.Entry(root)
name_entry.pack(padx=10, fill="x")

tk.Label(root, text="Email:").pack(anchor="w", padx=10, pady=(10, 0))
email_entry = tk.Entry(root)
email_entry.pack(padx=10, fill="x")

tk.Label(root, text="Destination:").pack(anchor="w", padx=10, pady=(10, 0))
destination_combo = ttk.Combobox(root, values=["Tenkasi", "Tirunelveli", "Coimbatore", "Tuticorin", "Kanyakumari"], state="readonly")
destination_combo.pack(padx=10, fill="x")

tk.Label(root, text="Number of Travelers:").pack(anchor="w", padx=10, pady=(10, 0))
travelers_spinbox = tk.Spinbox(root, from_=1, to=10)
travelers_spinbox.pack(padx=10, fill="x")

tk.Button(root, text="Confirm Booking", command=confirm_booking).pack(pady=15)

result_label = tk.Label(root, text="", justify="left", fg="green")
result_label.pack(padx=10, pady=10)

root.mainloop()
