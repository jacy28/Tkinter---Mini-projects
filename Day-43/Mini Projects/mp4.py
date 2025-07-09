# ✅ 4. Split Screen Email Client UI
# Objective: Simulate an email reading interface.
# Requirements:
# •	Use PanedWindow (horizontal): left pane = inbox list; right pane = message preview.
# •	Menu: File > Compose, Exit.
# •	Toolbar: Buttons for Reply, Forward, Delete.
# •	On "Compose", open a custom dialog using Toplevel().

import tkinter as tk
from tkinter import messagebox, Toplevel

def compose_email():
    compose_win = Toplevel(root)
    compose_win.title("Compose Email")
    compose_win.geometry("400x300")

    tk.Label(compose_win, text="To:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
    tk.Entry(compose_win, width=40).grid(row=0, column=1, padx=5, pady=5)

    tk.Label(compose_win, text="Subject:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
    tk.Entry(compose_win, width=40).grid(row=1, column=1, padx=5, pady=5)

    tk.Label(compose_win, text="Message:").grid(row=2, column=0, sticky="nw", padx=5, pady=5)
    tk.Text(compose_win, height=10, width=40).grid(row=2, column=1, padx=5, pady=5)

    tk.Button(compose_win, text="Send", command=lambda: messagebox.showinfo("Sent", "Email sent successfully")).grid(row=3, column=1, pady=10, sticky="e")

def show_message(event):
    selected = inbox_listbox.get(inbox_listbox.curselection())
    message_text.delete(1.0, tk.END)
    message_text.insert(tk.END, f"Preview of '{selected}'\n\nThis is the content of the selected message.")

def dummy_action():
    messagebox.showinfo("Info", "This feature is a placeholder.")

def on_exit():
    if messagebox.askokcancel("Exit", "Exit the application?"):
        root.destroy()

root = tk.Tk()
root.title("Email Client UI")
root.geometry("700x400")

# Menu
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Compose", command=compose_email)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=on_exit)
menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)

# Toolbar
toolbar = tk.Frame(root, bd=1, relief="raised")
tk.Button(toolbar, text="Reply", command=dummy_action).pack(side="left", padx=2, pady=2)
tk.Button(toolbar, text="Forward", command=dummy_action).pack(side="left", padx=2, pady=2)
tk.Button(toolbar, text="Delete", command=dummy_action).pack(side="left", padx=2, pady=2)
toolbar.pack(side="top", fill="x")

# PanedWindow
paned_window = tk.PanedWindow(root, sashrelief="sunken", sashwidth=5)
paned_window.pack(fill="both", expand=True)

# Left Pane (Inbox)
inbox_frame = tk.Frame(paned_window)
inbox_listbox = tk.Listbox(inbox_frame)
inbox_listbox.pack(fill="both", expand=True)
for i in range(1, 11):
    inbox_listbox.insert(tk.END, f"Email Subject {i}")
inbox_listbox.bind("<<ListboxSelect>>", show_message)
paned_window.add(inbox_frame, minsize=200)

# Right Pane (Message Preview)
preview_frame = tk.Frame(paned_window)
message_text = tk.Text(preview_frame, wrap="word")
message_text.pack(fill="both", expand=True)
paned_window.add(preview_frame)

root.protocol("WM_DELETE_WINDOW", on_exit)
root.mainloop()
