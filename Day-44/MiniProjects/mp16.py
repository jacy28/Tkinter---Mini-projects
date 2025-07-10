# ✅ 16. Resizable Panel with State Controls
# Objective: Enable/disable widgets inside a panel dynamically.
# Features:
# •	Frame with multiple Entry and Button widgets.
# •	External Toggle button to disable/enable the entire frame content.

import tkinter as tk

def toggle_panel():
    state = "normal" if toggle_btn.config('text')[-1] == "Enable Panel" else "disabled"
    for widget in panel.winfo_children():
        widget.config(state=state)
    toggle_btn.config(text="Enable Panel" if state == "disabled" else "Disable Panel")

root = tk.Tk()
root.geometry("300x250")
root.title("Resizable Panel Control")

panel = tk.Frame(root, bd=2, relief="groove")
panel.pack(padx=10, pady=10, fill="x")

entries = [tk.Entry(panel) for _ in range(2)]
buttons = [tk.Button(panel, text="OK") for _ in range(2)]
for e in entries: e.pack(pady=2)
for b in buttons: b.pack(pady=2)

toggle_btn = tk.Button(root, text="Disable Panel", command=toggle_panel)
toggle_btn.pack(pady=10)

root.mainloop()
