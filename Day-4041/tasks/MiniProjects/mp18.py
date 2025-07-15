# 🎤 18. Voice Command Logger
# Goal: Simulate voice command capture (manual typing for now).
# Requirements:
# •	Entry for “simulated command”.
# •	Button to log it in Text.
# •	Show number of commands entered.
# •	Use Label to show dynamic count.

import tkinter as tk

# Initialize command list
commands = []

def log_command():
    cmd = command_entry.get().strip()
    if cmd:
        commands.append(cmd)
        count_label.config(text=f"Commands Logged: {len(commands)}")
        command_entry.delete(0, tk.END)

# Main Window
root = tk.Tk()
root.title("🎤 Voice Command Logger")
root.geometry("350x200")

# Widgets
tk.Label(root, text="Enter Simulated Voice Command:").pack(pady=10)

command_entry = tk.Entry(root, width=40)
command_entry.pack(pady=5)

log_button = tk.Button(root, text="Log Command", command=log_command)
log_button.pack(pady=10)

count_label = tk.Label(root, text="Commands Logged: 0", font=("Arial", 12, "bold"))
count_label.pack(pady=10)

root.mainloop()
