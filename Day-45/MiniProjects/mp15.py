# 🔰 15. File Format Converter (.txt to .csv)
# Goal: Load .txt, convert, and save as .csv.
# Requirements:
# •	File open via filedialog.
# •	Parse text data into structured format.
# •	Save output using asksaveasfilename().

import tkinter as tk
from tkinter import filedialog, messagebox
import csv

def load_txt():
    path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if path:
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        data.clear()
        for line in lines:
            row = line.strip().split(",")  # or use "\t" if tab-delimited
            data.append(row)
        status_label.config(text=f"Loaded {len(data)} rows")

def save_csv():
    if not data:
        messagebox.showerror("No Data", "Load a .txt file first.")
        return
    path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if path:
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(data)
        status_label.config(text=f"Saved as {path}")

root = tk.Tk()
root.title("File Format Converter (.txt to .csv)")
root.geometry("400x200")

data = []

tk.Button(root, text="Load .txt File", command=load_txt).pack(pady=15)
tk.Button(root, text="Save as .csv", command=save_csv).pack(pady=10)

status_label = tk.Label(root, text="")
status_label.pack(pady=20)

root.mainloop()
