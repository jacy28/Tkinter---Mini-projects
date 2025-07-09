# ✅ 2. Text Editor App (Mini Notepad)
# Objective: Build a Notepad-like text editor with file operations.
# Requirements:
# •	Use Frames to separate the toolbar and text area.
# •	Add Menu with File > New, Open, Save, Exit.
# •	Add a Toolbar with Open and Save buttons.
# •	Use Text widget for multi-line editing.
# •	Show confirmation dialog on exit using messagebox.

import tkinter as tk
from tkinter import filedialog, messagebox

def new_file():
    if confirm_discard_changes():
        text_area.delete(1.0, tk.END)
        root.title("Untitled - Mini Notepad")

def open_file():
    if confirm_discard_changes():
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, content)
            root.title(f"{file_path} - Mini Notepad")

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            content = text_area.get(1.0, tk.END)
            file.write(content)
        root.title(f"{file_path} - Mini Notepad")

def confirm_discard_changes():
    return messagebox.askokcancel("Confirm", "Discard current changes?")

def on_exit():
    if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
        root.destroy()

root = tk.Tk()
root.title("Mini Notepad")
root.geometry("600x400")

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=on_exit)
menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)

toolbar_frame = tk.Frame(root, bd=1, relief="raised")
tk.Button(toolbar_frame, text="Open", command=open_file).pack(side="left", padx=2, pady=2)
tk.Button(toolbar_frame, text="Save", command=save_file).pack(side="left", padx=2, pady=2)
toolbar_frame.pack(side="top", fill="x")

text_area = tk.Text(root, wrap="word", undo=True)
text_area.pack(fill="both", expand=True, padx=5, pady=5)

root.protocol("WM_DELETE_WINDOW", on_exit)
root.mainloop()
