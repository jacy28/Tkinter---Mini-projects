# 32. Bulk File Renamer Tool with Pattern Matching
# •	Select files/folder
# •	Preview renaming with pattern (e.g., IMG_##)
# •	Apply sequential numbers, date tags
# •	Undo renaming
# •	Export log file

import os
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from datetime import datetime

class BulkRenamer:
    def __init__(self, root):
        self.root = root
        self.root.title("Bulk File Renamer Tool")

        self.files = []
        self.prev_names = []
        self.log = []

        self.build_ui()

    def build_ui(self):
        frame = tk.Frame(self.root)
        frame.pack(padx=10, pady=10)

        tk.Button(frame, text="Select Files", command=self.select_files).grid(row=0, column=0)
        tk.Button(frame, text="Select Folder", command=self.select_folder).grid(row=0, column=1)
        tk.Button(frame, text="Preview Rename", command=self.preview_rename).grid(row=0, column=2)
        tk.Button(frame, text="Apply Rename", command=self.apply_rename).grid(row=0, column=3)
        tk.Button(frame, text="Undo Rename", command=self.undo_rename).grid(row=0, column=4)
        tk.Button(frame, text="Export Log", command=self.export_log).grid(row=0, column=5)

        self.pattern_entry = tk.Entry(frame, width=50)
        self.pattern_entry.insert(0, "IMG_##_DATE")  # Default pattern
        self.pattern_entry.grid(row=1, column=0, columnspan=6, pady=10)

        self.listbox = tk.Listbox(self.root, width=100)
        self.listbox.pack(padx=10, pady=10)

    def select_files(self):
        self.files = filedialog.askopenfilenames()
        self.refresh_listbox()

    def select_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.files = [os.path.join(folder, f) for f in os.listdir(folder)
                          if os.path.isfile(os.path.join(folder, f))]
            self.refresh_listbox()

    def refresh_listbox(self):
        self.listbox.delete(0, tk.END)
        for f in self.files:
            self.listbox.insert(tk.END, f)

    def get_new_names(self):
        pattern = self.pattern_entry.get()
        new_names = []
        date_str = datetime.now().strftime("%Y%m%d")
        digits = pattern.count("#")
        counter_format = f"{{:0{digits}d}}"

        for i, path in enumerate(self.files):
            folder, original = os.path.split(path)
            ext = os.path.splitext(original)[1]
            count_str = counter_format.format(i + 1)
            name = pattern.replace("#" * digits, count_str).replace("DATE", date_str)
            new_names.append(os.path.join(folder, name + ext))
        return new_names

    def preview_rename(self):
        if not self.files:
            return messagebox.showwarning("No files", "Please select files or folder first.")
        new_names = self.get_new_names()
        self.listbox.delete(0, tk.END)
        for old, new in zip(self.files, new_names):
            self.listbox.insert(tk.END, f"{os.path.basename(old)} ➝ {os.path.basename(new)}")

    def apply_rename(self):
        if not self.files:
            return messagebox.showwarning("No files", "Please select files or folder first.")
        new_names = self.get_new_names()
        self.prev_names = list(self.files)
        self.log = []

        try:
            for old, new in zip(self.files, new_names):
                os.rename(old, new)
                self.log.append(f"{old} -> {new}")
            self.files = new_names
            messagebox.showinfo("Success", "Files renamed successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Rename failed: {e}")
        self.refresh_listbox()

    def undo_rename(self):
        if not self.prev_names:
            return messagebox.showwarning("Nothing to undo", "No previous rename found.")
        try:
            for current, old in zip(self.files, self.prev_names):
                os.rename(current, old)
                self.log.append(f"UNDO: {current} -> {old}")
            self.files = self.prev_names
            self.prev_names = []
            messagebox.showinfo("Undo", "Rename undone.")
        except Exception as e:
            messagebox.showerror("Error", f"Undo failed: {e}")
        self.refresh_listbox()

    def export_log(self):
        if not self.log:
            return messagebox.showwarning("No log", "Nothing to export.")
        path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text File", "*.txt")])
        if path:
            with open(path, 'w') as f:
                f.write("\n".join(self.log))
            messagebox.showinfo("Exported", f"Log saved to {path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BulkRenamer(root)
    root.mainloop()
