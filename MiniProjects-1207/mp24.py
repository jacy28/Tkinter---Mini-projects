# 44. Process Manager (View & Terminate Processes)
# •	List all running processes using psutil
# •	Search/filter processes
# •	Show CPU/RAM usage per process
# •	Terminate process button
# •	Refresh every few seconds

import tkinter as tk
from tkinter import ttk, messagebox
import psutil

REFRESH_INTERVAL = 3000  # ms

def get_processes(filter_text=""):
    process_list = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            if filter_text.lower() in proc.info['name'].lower():
                process_list.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return sorted(process_list, key=lambda x: x['cpu_percent'], reverse=True)

def refresh_processes():
    for row in tree.get_children():
        tree.delete(row)

    processes = get_processes(search_var.get())
    for proc in processes:
        tree.insert("", tk.END, values=(
            proc['pid'],
            proc['name'],
            f"{proc['cpu_percent']:.1f}%",
            f"{proc['memory_percent']:.1f}%"
        ))

    root.after(REFRESH_INTERVAL, refresh_processes)

def terminate_selected():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("No Selection", "Select a process to terminate.")
        return
    pid = tree.item(selected[0])['values'][0]
    try:
        p = psutil.Process(pid)
        p.terminate()
        messagebox.showinfo("Terminated", f"Process PID {pid} terminated.")
        refresh_processes()
    except (psutil.NoSuchProcess, psutil.AccessDenied, Exception) as e:
        messagebox.showerror("Error", f"Could not terminate process: {e}")

def on_search(*args):
    refresh_processes()

# ---------------- UI Setup ---------------- #
root = tk.Tk()
root.title("Process Manager")
root.geometry("700x500")

# Search bar
search_var = tk.StringVar()
search_var.trace_add("write", on_search)
tk.Entry(root, textvariable=search_var, font=("Segoe UI", 12), width=40).pack(pady=10)

# Treeview setup
columns = ("PID", "Name", "CPU %", "RAM %")
tree = ttk.Treeview(root, columns=columns, show="headings", height=20)
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center", width=150 if col != "Name" else 250)
tree.pack(fill=tk.BOTH, expand=True)

# Terminate Button
tk.Button(root, text="Terminate Selected Process", command=terminate_selected,
          font=("Segoe UI", 11), bg="red", fg="white").pack(pady=10)

# Start auto refresh
refresh_processes()

root.mainloop()
