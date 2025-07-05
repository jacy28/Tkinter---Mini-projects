# 🟢 16. Event Logger
# Goal: Log all mouse and keyboard events.
# Requirements:
# •	Bind <Key>, <Button-1>, <Double-Button-1> to log area.
# •	Use Text or Listbox to display event logs.
# •	Scrollbar for overflow.
# •	Button to clear logs

import tkinter as tk

def log_event(event):
    event_info = f"{event.type} - {event.keysym if event.type == '2' else event.num} at ({event.x},{event.y})"
    log_text.insert(tk.END, event_info + "\n")
    log_text.see(tk.END)

def clear_logs():
    log_text.delete("1.0", tk.END)

root = tk.Tk()
root.title("Event Logger")
root.geometry("500x400")

frame = tk.Frame(root)
frame.grid(row=0, column=0, padx=10, pady=10)

log_text = tk.Text(frame, width=60, height=20, wrap="none")
log_text.grid(row=0, column=0)

scrollbar = tk.Scrollbar(frame, command=log_text.yview)
scrollbar.grid(row=0, column=1, sticky="ns")
log_text.config(yscrollcommand=scrollbar.set)

clear_btn = tk.Button(root, text="Clear Logs", command=clear_logs)
clear_btn.grid(row=1, column=0, pady=10)

root.bind("<Key>", log_event)
root.bind("<Button-1>", log_event)
root.bind("<Double-Button-1>", log_event)

root.mainloop()
