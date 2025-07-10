# 🔰 13. Real-Time Logger App (Text + Thread)
# Goal: Simulate logging with real-time updates.
# Requirements:
# •	Start thread to generate logs.
# •	Use Text widget to show logs.
# •	Use after() to append text.
# •	Stop logging via button.

import tkinter as tk
import threading
import time
import random

running = False

def start_logging():
    global running
    if not running:
        running = True
        threading.Thread(target=generate_logs, daemon=True).start()

def stop_logging():
    global running
    running = False

def generate_logs():
    count = 1
    while running:
        log = f"[Log {count}] Event at {time.strftime('%H:%M:%S')}: Status {random.randint(100,999)}\n"
        root.after(0, lambda l=log: append_log(l))
        time.sleep(1)
        count += 1

def append_log(text):
    log_text.insert(tk.END, text)
    log_text.see(tk.END)

root = tk.Tk()
root.title("Real-Time Logger App")
root.geometry("500x400")

log_text = tk.Text(root, wrap="word", state="normal")
log_text.pack(expand=True, fill="both", padx=10, pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

tk.Button(btn_frame, text="Start Logging", command=start_logging).pack(side="left", padx=10)
tk.Button(btn_frame, text="Stop Logging", command=stop_logging).pack(side="left", padx=10)

root.mainloop()
