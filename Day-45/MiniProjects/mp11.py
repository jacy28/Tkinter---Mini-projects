# 🔰 11. Directory Backup Utility (FileDialog + Thread)
# Goal: Copy .txt files from source to backup folder.
# Requirements:
# •	Select source and target folder.
# •	Use thread to perform copy (with delay simulation).
# •	Display copied file count with after().

import os
import shutil
import time
import threading
import tkinter as tk
from tkinter import filedialog

def select_source():
    path = filedialog.askdirectory()
    if path:
        source_var.set(path)

def select_target():
    path = filedialog.askdirectory()
    if path:
        target_var.set(path)

def start_backup():
    src = source_var.get()
    dst = target_var.get()
    if not os.path.isdir(src) or not os.path.isdir(dst):
        status_label.config(text="Select valid folders.")
        return
    backup_btn.config(state="disabled")
    status_label.config(text="Backing up...")
    threading.Thread(target=copy_files, args=(src, dst), daemon=True).start()

def copy_files(src, dst):
    count = 0
    for filename in os.listdir(src):
        if filename.lower().endswith(".txt"):
            src_path = os.path.join(src, filename)
            dst_path = os.path.join(dst, filename)
            time.sleep(1)
            shutil.copy2(src_path, dst_path)
            count += 1
            root.after(0, lambda c=count: status_label.config(text=f"Copied: {c} file(s)"))
    root.after(0, lambda: backup_btn.config(state="normal"))

root = tk.Tk()
root.title("Directory Backup Utility")
root.geometry("500x250")

source_var = tk.StringVar()
target_var = tk.StringVar()

tk.Label(root, text="Source Folder").pack()
tk.Entry(root, textvariable=source_var, width=60).pack(padx=10)
tk.Button(root, text="Browse", command=select_source).pack(pady=5)

tk.Label(root, text="Backup Folder").pack()
tk.Entry(root, textvariable=target_var, width=60).pack(padx=10)
tk.Button(root, text="Browse", command=select_target).pack(pady=5)

backup_btn = tk.Button(root, text="Start Backup", command=start_backup)
backup_btn.pack(pady=10)

status_label = tk.Label(root, text="Status: Waiting")
status_label.pack(pady=10)

root.mainloop()
