# 10.	Text File Viewer
# Entry for file path, Button to load, and a Text widget to display the contents of the file.

import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

def load_file():
    filepath = file_entry.get()

    try:
        with open(filepath, "r") as file:
            content = file.read()
            text_widget.delete("1.0", tk.END)
            text_widget.insert(tk.END, content)
    except FileNotFoundError:
        messagebox.showerror("File Not Found", "The specified file could not be found.")
    except Exception as e:
        messagebox.showerror("Error", f"Could not load file:\n{str(e)}")

def browse_file():
    filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if filepath:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, filepath)

# GUI Setup
root = tk.Tk()
root.title("Text File Viewer")
root.geometry("600x400")

tk.Label(root, text="File Path:").pack(pady=5)

file_frame = tk.Frame(root)
file_frame.pack(pady=5)

file_entry = tk.Entry(file_frame, width=50)
file_entry.pack(side="left", padx=5)

browse_button = tk.Button(file_frame, text="Browse", command=browse_file)
browse_button.pack(side="left")

load_button = tk.Button(root, text="Load File", command=load_file)
load_button.pack(pady=10)

text_widget = tk.Text(root, wrap="word", width=70, height=15)
text_widget.pack(padx=10, pady=10, expand=True)

# Scrollbar
scrollbar = tk.Scrollbar(root, command=text_widget.yview)
scrollbar.pack(side="right", fill="y")
text_widget.config(yscrollcommand=scrollbar.set)

root.mainloop()
