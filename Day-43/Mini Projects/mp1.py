# ✅ 1. File Manager GUI
# Objective: Create a basic file explorer interface.
# Requirements:
# •	Use a PanedWindow: left pane for directory tree, right pane for file list.
# •	Include a Menu bar with options: File > Open, Exit.
# •	Add a Toolbar with buttons: Refresh, Open Folder.
# •	Display messages using messagebox.showinfo() or askquestion().

import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# === Functions ===
def refresh_file_list(path=None):
    if not path:
        path = os.getcwd()
    try:
        file_listbox.delete(0, tk.END)
        for item in os.listdir(path):
            file_listbox.insert(tk.END, item)
        current_dir.set(path)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def open_folder():
    folder = filedialog.askdirectory()
    if folder:
        refresh_file_list(folder)

def on_exit():
    if messagebox.askquestion("Exit", "Are you sure you want to exit?") == "yes":
        root.quit()

def show_info():
    messagebox.showinfo("Info", "Basic File Manager GUI")

# === Main Window ===
root = tk.Tk()
root.title("File Manager GUI")
root.geometry("700x400")

current_dir = tk.StringVar()

# === Menu Bar ===
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open Folder", command=open_folder)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=on_exit)
menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)

# === Toolbar ===
toolbar = tk.Frame(root, bd=1, relief="raised")
tk.Button(toolbar, text="Refresh", command=lambda: refresh_file_list(current_dir.get())).pack(side="left", padx=2, pady=2)
tk.Button(toolbar, text="Open Folder", command=open_folder).pack(side="left", padx=2, pady=2)
toolbar.pack(side="top", fill="x")

# === PanedWindow ===
paned = tk.PanedWindow(root, orient=tk.HORIZONTAL, sashrelief="raised")
paned.pack(fill="both", expand=True)

# Left Frame: Directory Tree (placeholder for now)
left_frame = tk.Frame(paned, bg="#f0f0f0", width=200)
tree_label = tk.Label(left_frame, text="Directory Tree (placeholder)")
tree_label.pack(padx=10, pady=10)
paned.add(left_frame)

# Right Frame: File List
right_frame = tk.Frame(paned)
tk.Label(right_frame, textvariable=current_dir, anchor="w").pack(fill="x", padx=5, pady=2)
file_listbox = tk.Listbox(right_frame)
file_listbox.pack(fill="both", expand=True, padx=5, pady=5)
paned.add(right_frame)

# === Initial Load ===
refresh_file_list()

root.mainloop()
