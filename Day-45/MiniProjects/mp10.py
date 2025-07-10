# 🔰 10. Customer Feedback Collector (SQLite + Multithread)
# Goal: Collect feedback with rating and store in SQLite.
# Requirements:
# •	Fields: Name, Rating (1–5), Comments.
# •	Submit stores feedback to database.
# •	Load all feedback into a Listbox.
# •	Simulate data submission delay using threads.

import tkinter as tk
from tkinter import messagebox
import sqlite3
import threading
import time

conn = sqlite3.connect("feedback.db")
cur = conn.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS feedback (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        rating INTEGER,
        comments TEXT
    )
""")
conn.commit()

def submit_feedback():
    name = name_var.get().strip()
    rating = rating_var.get().strip()
    comments = comment_box.get("1.0", tk.END).strip()
    if not name or not rating.isdigit() or not (1 <= int(rating) <= 5):
        messagebox.showerror("Error", "Enter valid Name and Rating (1–5).")
        return
    submit_btn.config(state="disabled")
    status_label.config(text="Submitting...")
    threading.Thread(target=simulate_submit, args=(name, rating, comments), daemon=True).start()

def simulate_submit(name, rating, comments):
    time.sleep(2)
    cur.execute("INSERT INTO feedback (name, rating, comments) VALUES (?, ?, ?)", (name, int(rating), comments))
    conn.commit()
    root.after(0, on_submit_complete)

def on_submit_complete():
    status_label.config(text="Submitted ✅")
    submit_btn.config(state="normal")
    load_feedback()
    name_var.set("")
    rating_var.set("")
    comment_box.delete("1.0", tk.END)

def load_feedback():
    listbox.delete(0, tk.END)
    rows = cur.execute("SELECT name, rating, comments FROM feedback").fetchall()
    for name, rating, comment in rows:
        listbox.insert(tk.END, f"{name} ({rating}/5): {comment}")

root = tk.Tk()
root.title("Customer Feedback Collector")
root.geometry("500x500")

name_var = tk.StringVar()
rating_var = tk.StringVar()

tk.Label(root, text="Name").pack()
tk.Entry(root, textvariable=name_var).pack(fill="x", padx=10)

tk.Label(root, text="Rating (1–5)").pack()
tk.Entry(root, textvariable=rating_var).pack(fill="x", padx=10)

tk.Label(root, text="Comments").pack()
comment_box = tk.Text(root, height=5)
comment_box.pack(fill="x", padx=10)

submit_btn = tk.Button(root, text="Submit Feedback", command=submit_feedback)
submit_btn.pack(pady=10)

status_label = tk.Label(root, text="")
status_label.pack()

tk.Label(root, text="Feedback Summary").pack(pady=(10, 0))
listbox = tk.Listbox(root, width=80)
listbox.pack(padx=10, pady=10, fill="both", expand=True)

load_feedback()
root.mainloop()
