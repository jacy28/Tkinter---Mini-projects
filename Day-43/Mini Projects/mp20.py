# ✅ 20. Event Logger Tool
# Objective: Log keypress and mouse click events.
# Requirements:
# •	Frame: Text area with scroll to show events.
# •	Menu: Events > Start Logging, Stop Logging.
# •	Toolbar: Clear log.
# •	Use .bind() to capture <Key>, <Button-1> and log to the text 

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Event Logger Tool")
root.geometry("600x400")

logging_enabled = False

# --- Toolbar ---
toolbar = tk.Frame(root, bd=1, relief="raised")
toolbar.pack(side="top", fill="x")

def clear_log():
    text_area.delete("1.0", tk.END)

clear_btn = tk.Button(toolbar, text="Clear Log", command=clear_log)
clear_btn.pack(side="left", padx=5, pady=5)

# --- Text Area with Scrollbar ---
text_frame = tk.Frame(root)
text_frame.pack(fill="both", expand=True)

scrollbar = tk.Scrollbar(text_frame)
scrollbar.pack(side="right", fill="y")

text_area = tk.Text(text_frame, wrap="word", yscrollcommand=scrollbar.set)
text_area.pack(fill="both", expand=True)
scrollbar.config(command=text_area.yview)

# --- Logging Events ---
def log_event(event):
    if logging_enabled:
        if event.type == tk.EventType.KeyPress:
            msg = f"Key Pressed: {event.keysym}\n"
        elif event.type == tk.EventType.ButtonPress:
            msg = f"Mouse Click at ({event.x}, {event.y})\n"
        else:
            return
        text_area.insert(tk.END, msg)
        text_area.see(tk.END)

def start_logging():
    global logging_enabled
    logging_enabled = True
    messagebox.showinfo("Logging", "Event logging started.")

def stop_logging():
    global logging_enabled
    logging_enabled = False
    messagebox.showinfo("Logging", "Event logging stopped.")

# --- Menu ---
menu = tk.Menu(root)
root.config(menu=menu)

event_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Events", menu=event_menu)
event_menu.add_command(label="Start Logging", command=start_logging)
event_menu.add_command(label="Stop Logging", command=stop_logging)

# --- Bind Events ---
root.bind("<Key>", log_event)
root.bind("<Button-1>", log_event)

root.mainloop()
