# ✅ 12. Event Logger Tool
# Scenario: Log all mouse clicks and keypresses.
# Features:
# •	Use .bind("<Key>") and .bind("<Button-1>").
# •	Display in Text widget.
# •	Scrollbar for long logs.
# •	Button to clear logs.

import tkinter as tk

def log_event(event):
    info = ""
    if event.type == tk.EventType.KeyPress:
        info = f"Key Pressed: {event.keysym}\n"
    elif event.type == tk.EventType.ButtonPress:
        info = f"Mouse Click at ({event.x}, {event.y})\n"
    log_text.insert(tk.END, info)
    log_text.see(tk.END)

def clear_logs():
    log_text.delete("1.0", tk.END)

root = tk.Tk()
root.title("Event Logger Tool")
root.geometry("400x300")

log_text = tk.Text(root, width=50, height=12)
log_text.pack(padx=10, pady=10, side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(root, command=log_text.yview)
scrollbar.pack(side="right", fill="y")
log_text.config(yscrollcommand=scrollbar.set)

tk.Button(root, text="Clear Logs", command=clear_logs).pack(pady=(0, 10))

root.bind("<Key>", log_event)
root.bind("<Button-1>", log_event)

root.mainloop()
