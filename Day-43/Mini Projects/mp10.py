# ✅ 10. Chat UI Layout
# Objective: Design a UI for a local chat application.
# Requirements:
# •	Use Frames: top = chat window (Text), bottom = entry field + send button.
# •	Toolbar: Connect, Disconnect.
# •	Menu: Chat > Clear, Exit.
# •	On Clear, ask confirmation using askokcancel() dialog.

import tkinter as tk
from tkinter import messagebox

def send_message():
    msg = entry_field.get()
    if msg:
        chat_window.insert(tk.END, "You: " + msg + "\n")
        entry_field.delete(0, tk.END)

def clear_chat():
    confirm = messagebox.askokcancel("Clear Chat", "Are you sure you want to clear the chat?")
    if confirm:
        chat_window.delete(1.0, tk.END)

root = tk.Tk()
root.title("Local Chat UI")
root.geometry("500x400")

# Menu bar
menubar = tk.Menu(root)
chat_menu = tk.Menu(menubar, tearoff=0)
chat_menu.add_command(label="Clear", command=clear_chat)
chat_menu.add_separator()
chat_menu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="Chat", menu=chat_menu)
root.config(menu=menubar)

# Toolbar
toolbar = tk.Frame(root, bg="#ddd")
toolbar.pack(side="top", fill="x")

tk.Button(toolbar, text="Connect").pack(side="left", padx=5, pady=5)
tk.Button(toolbar, text="Disconnect").pack(side="left", padx=5, pady=5)

# Chat display area
chat_frame = tk.Frame(root)
chat_frame.pack(fill="both", expand=True)

chat_window = tk.Text(chat_frame, state="normal", wrap="word")
chat_window.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(chat_frame, command=chat_window.yview)
scrollbar.pack(side="right", fill="y")
chat_window.config(yscrollcommand=scrollbar.set)

# Message input area
input_frame = tk.Frame(root)
input_frame.pack(fill="x")

entry_field = tk.Entry(input_frame)
entry_field.pack(side="left", fill="x", expand=True, padx=5, pady=5)

send_btn = tk.Button(input_frame, text="Send", command=send_message)
send_btn.pack(side="right", padx=5, pady=5)

root.mainloop()
