# ✅ 2. Survey Form with Conditional Disabling
# Objective: Disable “Next” button until all radio options are selected.
# Features:
# •	Label + Radiobutton options for 2 questions.
# •	Button for “Next” disabled by default.
# •	Dynamically check if both answers are selected using IntVar() and enable button.


import tkinter as tk
root=tk.Tk()
root.geometry("300x300")
import tkinter as tk

def check_selection(*args):
    if q1_var.get() != 0 and q2_var.get() != 0:
        next_btn.config(state="normal")
    else:
        next_btn.config(state="disabled")

q1_var = tk.IntVar()
q2_var = tk.IntVar()
q1_var.trace_add("write", check_selection)
q2_var.trace_add("write", check_selection)

tk.Label(root, text="1. Do you like Python?").pack(anchor="w")
tk.Radiobutton(root, text="Yes", variable=q1_var, value=1).pack(anchor="w")
tk.Radiobutton(root, text="No", variable=q1_var, value=2).pack(anchor="w")

tk.Label(root, text="2. Do you use Tkinter?").pack(anchor="w")
tk.Radiobutton(root, text="Yes", variable=q2_var, value=1).pack(anchor="w")
tk.Radiobutton(root, text="No", variable=q2_var, value=2).pack(anchor="w")

next_btn = tk.Button(root, text="Next", state="disabled")
next_btn.pack(pady=10)

root.mainloop()

root.mainloop()