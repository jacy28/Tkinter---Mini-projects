# 🔰 9. Notepad with Save Confirmation (Text + Dialog)
# Goal: Prompt save confirmation on exit.
# Requirements:
# •	Text editor using Text widget.
# •	File Save with asksaveasfilename().
# •	On window close, prompt to save changes with messagebox.askyesno().

import tkinter as tk
from tkinter import filedialog, messagebox

def save_file():
    file = filedialog.asksaveasfilename(defaultextension=".txt",
                                         filetypes=[("Text files", "*.txt")])
    if file:
        with open(file, "w", encoding="utf-8") as f:
            f.write(text_area.get(1.0, tk.END))
        root.title(f"Notepad - {file}")
        root.saved = True

def on_close():
    if not root.saved:
        answer = messagebox.askyesno("Save", "Do you want to save changes?")
        if answer:
            save_file()
    root.destroy()

root = tk.Tk()
root.title("Notepad")
root.geometry("600x400")
root.saved = False

text_area = tk.Text(root, wrap="word")
text_area.pack(expand=True, fill="both")

menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Save", command=save_file)

text_area.bind("<Key>", lambda e: setattr(root, 'saved', False))
root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()
