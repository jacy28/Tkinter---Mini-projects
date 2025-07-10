# 🔰 7. Background Data Fetcher UI (Thread + after())
# Goal: Fake API data fetch and update GUI without freezing.
# Requirements:
# •	Button to fetch data (simulate delay).
# •	Show "Fetching..." message.
# •	Use after() to safely update label with results.

import tkinter as tk
import threading
import time

def fetch_data():
    status_label.config(text="Fetching...")
    threading.Thread(target=simulate_fetch, daemon=True).start()

def simulate_fetch():
    time.sleep(3)
    result = "✅ Fake API Data: {'user': 'Alice', 'age': 30}"
    root.after(0, lambda: status_label.config(text=result))

root = tk.Tk()
root.title("Background Data Fetcher")
root.geometry("400x200")

tk.Button(root, text="Fetch Data", command=fetch_data).pack(pady=20)

status_label = tk.Label(root, text="Idle", font=("Arial", 12))
status_label.pack(pady=10)

root.mainloop()
