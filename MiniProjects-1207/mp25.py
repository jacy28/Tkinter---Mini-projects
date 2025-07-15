# 45. Clipboard Manager with History and Search
# •	Monitor clipboard content
# •	Save history in SQLite
# •	Search and reuse clipboard items
# •	Copy back to clipboard
# •	Option to export log

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import sqlite3
import pyperclip
import time
import threading

DB_NAME = "clipboard_history.db"

# ---------------- Database Setup ---------------- #
def setup_database():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS clipboard (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

# ---------------- Clipboard Monitor ---------------- #
def monitor_clipboard():
    recent = ""
    while True:
        try:
            current = pyperclip.paste()
            if current != recent and current.strip() != "":
                save_to_db(current)
                recent = current
                update_listbox()
        except:
            pass
        time.sleep(1)

def save_to_db(content):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO clipboard (content) VALUES (?)", (content,))
    conn.commit()
    conn.close()

# ---------------- UI Functions ---------------- #
def update_listbox(filter_text=""):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    if filter_text:
        c.execute("SELECT content FROM clipboard WHERE content LIKE ? ORDER BY id DESC", ('%' + filter_text + '%',))
    else:
        c.execute("SELECT content FROM clipboard ORDER BY id DESC LIMIT 100")
    rows = c.fetchall()
    conn.close()
    
    listbox.delete(0, tk.END)
    for row in rows:
        listbox.insert(tk.END, row[0])

def on_select(event):
    selected = listbox.curselection()
    if selected:
        content = listbox.get(selected[0])
        pyperclip.copy(content)
        messagebox.showinfo("Copied", "Text copied to clipboard!")

def on_search(*args):
    update_listbox(search_var.get())

def export_to_txt():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT content, timestamp FROM clipboard ORDER BY id DESC")
    rows = c.fetchall()
    conn.close()

    filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if filepath:
        with open(filepath, "w", encoding="utf-8") as f:
            for row in rows:
                f.write(f"[{row[1]}] {row[0]}\n")
        messagebox.showinfo("Exported", f"Clipboard history exported to:\n{filepath}")

# ---------------- GUI Setup ---------------- #
setup_database()

root = tk.Tk()
root.title("Clipboard Manager")
root.geometry("500x600")

tk.Label(root, text="Clipboard History", font=("Segoe UI", 14, "bold")).pack(pady=5)

search_var = tk.StringVar()
search_var.trace_add("write", on_search)
tk.Entry(root, textvariable=search_var, font=("Segoe UI", 12), width=40).pack(pady=5)

listbox = tk.Listbox(root, font=("Segoe UI", 11), width=60, height=25)
listbox.pack(pady=10)
listbox.bind("<<ListboxSelect>>", on_select)

tk.Button(root, text="Export to TXT", command=export_to_txt, font=("Segoe UI", 11)).pack(pady=10)

# ---------------- Start Monitoring Thread ---------------- #
threading.Thread(target=monitor_clipboard, daemon=True).start()

update_listbox()

root.mainloop()
