# 35. Scheduled File Backup Utility
# •	Select source and destination folders
# •	Choose frequency: hourly, daily
# •	Save config to SQLite
# •	Log backup status
# •	Optional: compress files to zip

import os
import shutil
import sqlite3
import zipfile
import threading
from tkinter import *
from tkinter import filedialog, messagebox
import time
import schedule
from datetime import datetime

# --- SQLite Setup ---
conn = sqlite3.connect("backup_config.db")
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS config (
    id INTEGER PRIMARY KEY,
    src TEXT,
    dest TEXT,
    freq TEXT,
    compress INTEGER
)''')
conn.commit()

# --- GUI ---
root = Tk()
root.title("Scheduled Backup Utility")
root.geometry("450x300")

src_folder = StringVar()
dest_folder = StringVar()
frequency = StringVar(value="Daily")
compress_var = IntVar()

# --- Functions ---

def choose_src():
    path = filedialog.askdirectory()
    if path:
        src_folder.set(path)

def choose_dest():
    path = filedialog.askdirectory()
    if path:
        dest_folder.set(path)

def save_config():
    c.execute("DELETE FROM config")
    c.execute("INSERT INTO config (src, dest, freq, compress) VALUES (?, ?, ?, ?)",
              (src_folder.get(), dest_folder.get(), frequency.get(), compress_var.get()))
    conn.commit()
    messagebox.showinfo("Saved", "Backup configuration saved.")

def log_status(msg):
    with open("backup_log.txt", "a") as f:
        f.write(f"{datetime.now()}: {msg}\n")

def do_backup():
    try:
        c.execute("SELECT src, dest, compress FROM config")
        row = c.fetchone()
        if not row:
            log_status("No config found.")
            return
        src, dest, compress = row
        if not os.path.exists(src) or not os.path.exists(dest):
            log_status("Invalid source or destination.")
            return

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        if compress:
            zip_name = os.path.join(dest, f"backup_{timestamp}.zip")
            with zipfile.ZipFile(zip_name, 'w') as zipf:
                for foldername, _, filenames in os.walk(src):
                    for filename in filenames:
                        file_path = os.path.join(foldername, filename)
                        arcname = os.path.relpath(file_path, src)
                        zipf.write(file_path, arcname)
            log_status(f"Backup (ZIP) completed: {zip_name}")
        else:
            backup_path = os.path.join(dest, f"backup_{timestamp}")
            shutil.copytree(src, backup_path)
            log_status(f"Backup completed: {backup_path}")
    except Exception as e:
        log_status(f"Error: {str(e)}")

def start_schedule():
    c.execute("SELECT freq FROM config")
    row = c.fetchone()
    if not row:
        messagebox.showwarning("Missing Config", "Save your configuration first.")
        return

    freq = row[0].lower()
    if freq == "hourly":
        schedule.every().hour.do(do_backup)
    else:
        schedule.every().day.at("00:00").do(do_backup)

    def run_scheduler():
        while True:
            schedule.run_pending()
            time.sleep(1)

    threading.Thread(target=run_scheduler, daemon=True).start()
    messagebox.showinfo("Scheduler Started", f"Backup scheduled ({freq}).")

# --- GUI Layout ---

Label(root, text="Source Folder").pack()
Entry(root, textvariable=src_folder, width=50).pack()
Button(root, text="Browse", command=choose_src).pack(pady=5)

Label(root, text="Destination Folder").pack()
Entry(root, textvariable=dest_folder, width=50).pack()
Button(root, text="Browse", command=choose_dest).pack(pady=5)

Label(root, text="Backup Frequency").pack()
OptionMenu(root, frequency, "Hourly", "Daily").pack(pady=5)

Checkbutton(root, text="Compress to ZIP", variable=compress_var).pack(pady=5)

Button(root, text="💾 Save Config", command=save_config).pack(pady=5)
Button(root, text="▶ Start Backup Schedule", command=start_schedule).pack(pady=5)

root.mainloop()
