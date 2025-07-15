# 25. Student Performance Tracker with Trend Analysis
# •	Add subjects and mark entries
# •	Track student performance over time
# •	Line chart of mark trends
# •	Average, median, top score computation
# •	Filter by subject or term

import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from statistics import mean, median
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# --- Setup database ---
conn = sqlite3.connect("student_marks.db")
c = conn.cursor()
c.execute("""
CREATE TABLE IF NOT EXISTS marks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student TEXT,
    subject TEXT,
    term TEXT,
    mark INTEGER
)""")
conn.commit()

# --- GUI Setup ---
root = tk.Tk()
root.title("Student Performance Tracker")

student_var = tk.StringVar()
subject_var = tk.StringVar()
term_var = tk.StringVar()
mark_var = tk.IntVar()

# --- Add Entry Section ---
entry_frame = ttk.Frame(root)
entry_frame.pack(pady=10)

ttk.Label(entry_frame, text="Student").grid(row=0, column=0)
ttk.Entry(entry_frame, textvariable=student_var, width=15).grid(row=0, column=1)

ttk.Label(entry_frame, text="Subject").grid(row=0, column=2)
ttk.Entry(entry_frame, textvariable=subject_var, width=15).grid(row=0, column=3)

ttk.Label(entry_frame, text="Term").grid(row=0, column=4)
ttk.Entry(entry_frame, textvariable=term_var, width=10).grid(row=0, column=5)

ttk.Label(entry_frame, text="Mark").grid(row=0, column=6)
ttk.Entry(entry_frame, textvariable=mark_var, width=5).grid(row=0, column=7)

def add_entry():
    if student_var.get() and subject_var.get() and term_var.get():
        c.execute("INSERT INTO marks (student, subject, term, mark) VALUES (?, ?, ?, ?)",
                  (student_var.get(), subject_var.get(), term_var.get(), mark_var.get()))
        conn.commit()
        student_var.set(""); subject_var.set(""); term_var.set(""); mark_var.set(0)
        refresh_data()
    else:
        messagebox.showwarning("Incomplete", "Please fill all fields.")

ttk.Button(entry_frame, text="Add", command=add_entry).grid(row=0, column=8, padx=5)

# --- Filter Section ---
filter_frame = ttk.Frame(root)
filter_frame.pack(pady=5)

filter_subject = tk.StringVar()
filter_term = tk.StringVar()

ttk.Label(filter_frame, text="Filter Subject:").pack(side="left")
ttk.Entry(filter_frame, textvariable=filter_subject, width=15).pack(side="left", padx=2)
ttk.Label(filter_frame, text="Term:").pack(side="left")
ttk.Entry(filter_frame, textvariable=filter_term, width=10).pack(side="left", padx=2)

# --- Treeview ---
tree = ttk.Treeview(root, columns=("Student", "Subject", "Term", "Mark"), show="headings")
for col in ("Student", "Subject", "Term", "Mark"):
    tree.heading(col, text=col)
tree.pack(pady=10, fill="x")

def refresh_data():
    for i in tree.get_children():
        tree.delete(i)
    c.execute("SELECT student, subject, term, mark FROM marks")
    for row in c.fetchall():
        tree.insert("", "end", values=row)

refresh_data()

# --- Stats and Chart ---
def show_stats():
    query = "SELECT mark FROM marks WHERE 1=1"
    params = []
    if filter_subject.get():
        query += " AND subject=?"
        params.append(filter_subject.get())
    if filter_term.get():
        query += " AND term=?"
        params.append(filter_term.get())

    c.execute(query, params)
    rows = [r[0] for r in c.fetchall()]
    if rows:
        msg = f"Average: {mean(rows):.2f} | Median: {median(rows):.2f} | Top: {max(rows)}"
        messagebox.showinfo("Statistics", msg)
    else:
        messagebox.showinfo("No Data", "No marks found.")

def show_chart():
    query = "SELECT term, mark FROM marks WHERE 1=1"
    params = []
    if filter_subject.get():
        query += " AND subject=?"
        params.append(filter_subject.get())
    if filter_term.get():
        query += " AND term=?"
        params.append(filter_term.get())

    query += " ORDER BY term"
    c.execute(query, params)
    rows = c.fetchall()

    if rows:
        terms, marks = zip(*rows)
        fig, ax = plt.subplots()
        ax.plot(terms, marks, marker='o')
        ax.set_title("Mark Trend")
        ax.set_ylabel("Marks")
        ax.set_xlabel("Term")
        chart_win = tk.Toplevel(root)
        chart_win.title("Trend Chart")
        chart = FigureCanvasTkAgg(fig, master=chart_win)
        chart.get_tk_widget().pack()
        chart.draw()
    else:
        messagebox.showinfo("No Data", "No marks found to plot.")

btn_frame = ttk.Frame(root)
btn_frame.pack(pady=5)
ttk.Button(btn_frame, text="Show Stats", command=show_stats).pack(side="left", padx=5)
ttk.Button(btn_frame, text="Show Trend", command=show_chart).pack(side="left", padx=5)

root.mainloop()

