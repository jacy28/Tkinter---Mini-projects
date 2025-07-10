# 🔰 2. Text File Editor (FileDialog + Text Widget)
# Goal: Load and edit .txt files.
# Requirements:
# •	Open File → Load file content into Text widget.
# •	Save File → Save edited content.
# •	Use filedialog to open/save files.
# •	Filter file types (.txt only).
# •	Show filename in the title bar.

import tkinter as tk
from tkinter import filedialog, messagebox

def open_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt")],
        defaultextension=".txt"
    )
    if file_path:
        try:
            with open(file_path, "r") as file:
                content = file.read()
            text.delete("1.0", tk.END)
            text.insert(tk.END, content)
            root.title(f"Text Editor - {file_path}")
            root.current_file = file_path
        except Exception as e:
            messagebox.showerror("Error", f"Could not open file:\n{e}")

def save_file():
    if hasattr(root, 'current_file') and root.current_file:
        file_path = root.current_file
    else:
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt")]
        )
        if not file_path:
            return
        root.current_file = file_path

    try:
        with open(file_path, "w") as file:
            file.write(text.get("1.0", tk.END))
        root.title(f"Text Editor - {file_path}")
        messagebox.showinfo("Saved", "File saved successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Could not save file:\n{e}")

root = tk.Tk()
root.title("Text Editor")
root.geometry("600x500")
root.current_file = None

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=False)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

text = tk.Text(root, wrap="word", font=("Arial", 12))
text.pack(fill="both", expand=True)

root.mainloop()
