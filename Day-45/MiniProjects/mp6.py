# 🔰 6. File Searcher (Directory + File Reading)
# Goal: Search for a keyword inside .txt files in a folder.
# Requirements:
# •	Select folder via askdirectory().
# •	Input keyword to search.
# •	Display list of file names and matching lines.
# •	Use multithreading for large folders.

import os
import threading
import tkinter as tk
from tkinter import filedialog

def select_folder():
    folder = filedialog.askdirectory()
    if folder:
        folder_var.set(folder)

def search_files():
    result_box.delete(0, tk.END)
    keyword = keyword_var.get().strip()
    folder = folder_var.get().strip()
    if not keyword or not folder:
        result_box.insert(tk.END, "Please provide both folder and keyword.")
        return
    threading.Thread(target=run_search, args=(folder, keyword), daemon=True).start()

def run_search(folder, keyword):
    for root_dir, _, files in os.walk(folder):
        for file in files:
            if file.lower().endswith(".txt"):
                try:
                    path = os.path.join(root_dir, file)
                    with open(path, 'r', encoding="utf-8", errors="ignore") as f:
                        for i, line in enumerate(f, 1):
                            if keyword.lower() in line.lower():
                                update_result(f"{file} (line {i}): {line.strip()}")
                except Exception as e:
                    update_result(f"Error reading {file}: {e}")

def update_result(text):
    result_box.after(0, lambda: result_box.insert(tk.END, text))

root = tk.Tk()
root.title("File Searcher")
root.geometry("600x500")

folder_var = tk.StringVar()
keyword_var = tk.StringVar()

tk.Label(root, text="Folder:").pack(anchor="w", padx=10)
tk.Entry(root, textvariable=folder_var, width=50).pack(padx=10, fill="x")
tk.Button(root, text="Browse", command=select_folder).pack(padx=10, pady=5)

tk.Label(root, text="Keyword:").pack(anchor="w", padx=10)
tk.Entry(root, textvariable=keyword_var, width=30).pack(padx=10, fill="x")

tk.Button(root, text="Search", command=search_files).pack(pady=10)

result_box = tk.Listbox(root, width=80, height=20)
result_box.pack(padx=10, pady=10, fill="both", expand=True)

root.mainloop()
