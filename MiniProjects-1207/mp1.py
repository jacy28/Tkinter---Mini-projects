# 21. CSV Data Analyzer with Charts and Summaries
# •	Upload CSV using askopenfilename()
# •	Parse and display data in Treeview
# •	Calculate total, average, min, max per column
# •	Visualize selected column as bar or pie chart
# •	Export summary report as PDF

import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas as pdf_canvas

# --- Setup ---
root = tk.Tk()
root.title("CSV Data Analyzer")
root.geometry("900x600")

data = None  # global DataFrame

# --- Upload CSV ---
def load_csv():
    global data
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if not file_path: 
        return
    try:
        data = pd.read_csv(file_path)
        update_treeview()
        update_column_list()
        update_summary()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# --- Display CSV in Treeview ---
def update_treeview():
    tree.delete(*tree.get_children())
    tree["columns"] = list(data.columns)
    tree["show"] = "headings"
    for col in data.columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)
    for index, row in data.iterrows():
        tree.insert("", "end", values=list(row))

# --- Update Column Selector ---
def update_column_list():
    numeric_cols = data.select_dtypes(include='number').columns.tolist()
    column_combo["values"] = numeric_cols
    if numeric_cols:
        column_combo.set(numeric_cols[0])

# --- Summary Calculation ---
def update_summary():
    summary_text.delete("1.0", tk.END)
    if data is None:
        return
    numeric_data = data.select_dtypes(include='number')
    for col in numeric_data.columns:
        summary_text.insert(tk.END, f"{col}:\n")
        summary_text.insert(tk.END, f"  ➤ Total: {numeric_data[col].sum()}\n")
        summary_text.insert(tk.END, f"  ➤ Average: {numeric_data[col].mean()}\n")
        summary_text.insert(tk.END, f"  ➤ Min: {numeric_data[col].min()}\n")
        summary_text.insert(tk.END, f"  ➤ Max: {numeric_data[col].max()}\n\n")

# --- Plotting ---
def plot_column(kind):
    col = column_combo.get()
    if col not in data.columns:
        return
    chart_ax.clear()
    if kind == "Bar":
        chart_ax.bar(data[col].index, data[col])
    elif kind == "Pie":
        chart_ax.pie(data[col].value_counts(), labels=data[col].value_counts().index, autopct='%1.1f%%')
    chart_ax.set_title(f"{kind} Chart of '{col}'")
    chart_canvas.draw()

# --- Export Summary as PDF ---
def export_summary_pdf():
    if data is None:
        return
    filename = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF", "*.pdf")])
    if not filename:
        return
    c = pdf_canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    c.setFont("Helvetica", 12)
    y = height - 40
    c.drawString(40, y, "CSV Summary Report")
    y -= 20

    numeric_data = data.select_dtypes(include='number')
    for col in numeric_data.columns:
        c.drawString(40, y, f"{col}:")
        y -= 15
        c.drawString(60, y, f"Total: {numeric_data[col].sum():.2f}")
        y -= 15
        c.drawString(60, y, f"Average: {numeric_data[col].mean():.2f}")
        y -= 15
        c.drawString(60, y, f"Min: {numeric_data[col].min():.2f}")
        y -= 15
        c.drawString(60, y, f"Max: {numeric_data[col].max():.2f}")
        y -= 25
        if y < 100:
            c.showPage()
            y = height - 40

    c.save()
    messagebox.showinfo("Success", "Summary exported to PDF.")

# --- UI Layout ---
top_frame = tk.Frame(root)
top_frame.pack(pady=10)

tk.Button(top_frame, text="📁 Load CSV", command=load_csv).pack(side=tk.LEFT, padx=5)

column_combo = ttk.Combobox(top_frame, width=20)
column_combo.pack(side=tk.LEFT, padx=5)

tk.Button(top_frame, text="📊 Bar Chart", command=lambda: plot_column("Bar")).pack(side=tk.LEFT, padx=5)
tk.Button(top_frame, text="🥧 Pie Chart", command=lambda: plot_column("Pie")).pack(side=tk.LEFT, padx=5)
tk.Button(top_frame, text="📝 Export PDF", command=export_summary_pdf).pack(side=tk.LEFT, padx=5)

# Treeview
tree = ttk.Treeview(root, height=10)
tree.pack(fill=tk.X, padx=10)

# Chart
chart_fig, chart_ax = plt.subplots(figsize=(5, 3))
chart_canvas = FigureCanvasTkAgg(chart_fig, master=root)
chart_canvas.get_tk_widget().pack()

# Summary box
summary_text = tk.Text(root, height=10, width=100)
summary_text.pack(pady=5)

root.mainloop()
