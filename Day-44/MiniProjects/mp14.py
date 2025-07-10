# ✅ 14. Custom Notification Widget
# Objective: Build a reusable notification widget class.
# Features:
# •	Class-based Frame with colored background.
# •	Includes icon (Label), message (Label), and close button.
# •	Appears at top and disappears after 5 seconds.

import tkinter as tk

class Notification(tk.Frame):
    def __init__(self, master, message, bg="lightyellow", fg="black", icon="🔔", **kwargs):
        super().__init__(master, bg=bg, padx=10, pady=5, **kwargs)

        self.icon_label = tk.Label(self, text=icon, bg=bg, fg=fg, font=("Arial", 14))
        self.icon_label.pack(side="left")

        self.message_label = tk.Label(self, text=message, bg=bg, fg=fg, font=("Arial", 12))
        self.message_label.pack(side="left", padx=5)

        self.close_btn = tk.Button(self, text="✖", command=self.destroy, bg=bg, fg=fg, bd=0)
        self.close_btn.pack(side="right")

        self.after(5000, self.destroy)

root = tk.Tk()
root.geometry("350x200")
root.title("Notification Example")

def show_notification():
    note = Notification(root, "This is a test notification!", bg="lightblue")
    note.pack(fill="x", pady=5)

tk.Button(root, text="Show Notification", command=show_notification).pack(pady=20)

root.mainloop()
