# 24. Budget Visualizer with Income/Expense Graphs
# •	Form to enter income/expense records
# •	Store in SQLite with category
# •	Monthly total, bar graph of categories
# •	Export financial report as CSV
# •	Pie chart for category-wise spend

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import sqlite3
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import csv
from datetime import datetime

DB_NAME = "budget.db"

class BudgetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Budget Visualizer")

        self.create_db()
        self.build_ui()
        self.refresh_table()

    def create_db(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                type TEXT,
                category TEXT,
                amount REAL,
                date TEXT
            )
        """)
        self.conn.commit()

    def build_ui(self):
        entry_frame = ttk.LabelFrame(self.root, text="Add Entry")
        entry_frame.pack(fill='x', padx=10, pady=5)

        self.type_var = tk.StringVar(value="Expense")
        self.category_var = tk.StringVar()
        self.amount_var = tk.DoubleVar()
        self.date_var = tk.StringVar(value=datetime.now().strftime('%Y-%m-%d'))

        ttk.Label(entry_frame, text="Type").grid(row=0, column=0)
        ttk.Combobox(entry_frame, textvariable=self.type_var, values=["Income", "Expense"], width=10).grid(row=0, column=1)

        ttk.Label(entry_frame, text="Category").grid(row=0, column=2)
        ttk.Entry(entry_frame, textvariable=self.category_var, width=15).grid(row=0, column=3)

        ttk.Label(entry_frame, text="Amount").grid(row=0, column=4)
        ttk.Entry(entry_frame, textvariable=self.amount_var, width=10).grid(row=0, column=5)

        ttk.Label(entry_frame, text="Date").grid(row=0, column=6)
        ttk.Entry(entry_frame, textvariable=self.date_var, width=12).grid(row=0, column=7)

        ttk.Button(entry_frame, text="Add", command=self.add_record).grid(row=0, column=8, padx=5)

        self.tree = ttk.Treeview(self.root, columns=("Type", "Category", "Amount", "Date"), show='headings')
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
        self.tree.pack(fill='both', expand=True, padx=10, pady=5)

        button_frame = ttk.Frame(self.root)
        button_frame.pack()

        ttk.Button(button_frame, text="Bar Graph", command=self.show_bar_graph).pack(side='left', padx=5)
        ttk.Button(button_frame, text="Pie Chart", command=self.show_pie_chart).pack(side='left', padx=5)
        ttk.Button(button_frame, text="Export CSV", command=self.export_csv).pack(side='left', padx=5)

    def add_record(self):
        try:
            self.cursor.execute("INSERT INTO records (type, category, amount, date) VALUES (?, ?, ?, ?)",
                (self.type_var.get(), self.category_var.get(), self.amount_var.get(), self.date_var.get()))
            self.conn.commit()
            self.refresh_table()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def refresh_table(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        self.cursor.execute("SELECT type, category, amount, date FROM records ORDER BY date DESC")
        for row in self.cursor.fetchall():
            self.tree.insert("", "end", values=row)

    def export_csv(self):
        file = filedialog.asksaveasfilename(defaultextension=".csv")
        if not file:
            return
        self.cursor.execute("SELECT * FROM records")
        with open(file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['ID', 'Type', 'Category', 'Amount', 'Date'])
            writer.writerows(self.cursor.fetchall())
        messagebox.showinfo("Exported", "Data exported successfully.")

    def show_bar_graph(self):
        self.cursor.execute("SELECT category, SUM(amount) FROM records WHERE type='Expense' GROUP BY category")
        data = self.cursor.fetchall()
        if not data:
            messagebox.showinfo("Info", "No expense data to show.")
            return
        categories, amounts = zip(*data)

        fig, ax = plt.subplots()
        ax.bar(categories, amounts, color='skyblue')
        ax.set_title("Expenses by Category")
        ax.set_ylabel("Amount")

        self.show_plot(fig)

    def show_pie_chart(self):
        self.cursor.execute("SELECT category, SUM(amount) FROM records WHERE type='Expense' GROUP BY category")
        data = self.cursor.fetchall()
        if not data:
            messagebox.showinfo("Info", "No data to show.")
            return
        categories, amounts = zip(*data)

        fig, ax = plt.subplots()
        ax.pie(amounts, labels=categories, autopct='%1.1f%%')
        ax.set_title("Expense Distribution")

        self.show_plot(fig)

    def show_plot(self, fig):
        top = tk.Toplevel(self.root)
        top.title("Chart")
        canvas = FigureCanvasTkAgg(fig, master=top)
        canvas.get_tk_widget().pack()
        canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = BudgetApp(root)
    root.mainloop()
