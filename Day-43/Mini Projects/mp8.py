# ✅ 8. PDF Merger Interface
# Objective: Merge multiple PDFs via UI.
# Requirements:
# •	Use PanedWindow (vertical): top = file list, bottom = log/preview.
# •	Toolbar: Add File, Remove File, Merge.
# •	Use Listbox to show selected files.
# •	On Merge, show status via messagebox.showinfo().

import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from PyPDF2 import PdfMerger

root = tk.Tk()
root.title("PDF Merger")
root.geometry("600x400")

pdf_files = []

def add_file():
    files = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
    for f in files:
        if f not in pdf_files:
            pdf_files.append(f)
            listbox.insert(tk.END, f)

def remove_file():
    selected = listbox.curselection()
    for i in reversed(selected):
        pdf_files.pop(i)
        listbox.delete(i)

def merge_pdfs():
    if not pdf_files:
        messagebox.showwarning("No Files", "Please add PDF files to merge.")
        return
    output_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
    if not output_path:
        return
    try:
        merger = PdfMerger()
        for file in pdf_files:
            merger.append(file)
        merger.write(output_path)
        merger.close()
        messagebox.showinfo("Success", f"PDFs merged successfully into:\n{output_path}")
        log_text.insert(tk.END, f"Merged into: {output_path}\n")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Toolbar
toolbar = tk.Frame(root)
toolbar.pack(fill="x")
tk.Button(toolbar, text="Add File", command=add_file).pack(side="left", padx=5, pady=5)
tk.Button(toolbar, text="Remove File", command=remove_file).pack(side="left", padx=5, pady=5)
tk.Button(toolbar, text="Merge", command=merge_pdfs).pack(side="left", padx=5, pady=5)

# PanedWindow
pane = tk.PanedWindow(root, orient=tk.VERTICAL)
pane.pack(fill="both", expand=True)

# Top - File List
file_frame = tk.Frame(pane)
listbox = tk.Listbox(file_frame, selectmode=tk.EXTENDED)
listbox.pack(fill="both", expand=True, padx=5, pady=5)
pane.add(file_frame)

# Bottom - Log/Preview
log_frame = tk.Frame(pane)
log_text = tk.Text(log_frame, height=5)
log_text.pack(fill="both", expand=True, padx=5, pady=5)
pane.add(log_frame)

root.mainloop()
