# 15. Library Book Issue System
# Objective: Issue books with user details.
# Features:
# •	Use Combobox for book titles.
# •	Entry for user name.
# •	Issue date via Spinbox (1–31).
# •	Listbox shows issued records.
# •	Scrollbar to manage large data.
# •	Layout with grid().

import tkinter as tk
from tkinter import ttk

def issue_book():
    user = user_entry.get()
    book = book_combo.get()
    date = date_spinbox.get()

    if user and book:
        record = f"{user} | {book} | Date: {date}"
        record_listbox.insert(tk.END, record)
        user_entry.delete(0, tk.END)
        book_combo.set("")
        date_spinbox.delete(0, tk.END)
        date_spinbox.insert(0, 1)

root = tk.Tk()
root.title("Library Book Issue System")
root.geometry("500x400")

tk.Label(root, text="User Name:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
user_entry = tk.Entry(root, width=30)
user_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Select Book:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
book_combo = ttk.Combobox(root, values=[
    "The Great Gatsby", "1984", "To Kill a Mockingbird",
    "Pride and Prejudice", "Moby Dick", "The Catcher in the Rye"
], state="readonly", width=27)
book_combo.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Issue Date (1-31):").grid(row=2, column=0, padx=10, pady=10, sticky="e")
date_spinbox = tk.Spinbox(root, from_=1, to=31, width=5)
date_spinbox.grid(row=2, column=1, padx=10, pady=10, sticky="w")
date_spinbox.delete(0, tk.END)
date_spinbox.insert(0, 1)

issue_btn = tk.Button(root, text="Issue Book", command=issue_book)
issue_btn.grid(row=3, column=0, columnspan=2, pady=10)

tk.Label(root, text="Issued Records:").grid(row=4, column=0, columnspan=2, pady=(10, 0))

list_frame = tk.Frame(root)
list_frame.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

record_listbox = tk.Listbox(list_frame, width=55, height=10)
record_listbox.pack(side="left", fill="y")

scrollbar = tk.Scrollbar(list_frame, orient="vertical", command=record_listbox.yview)
scrollbar.pack(side="right", fill="y")
record_listbox.config(yscrollcommand=scrollbar.set)

root.mainloop()
