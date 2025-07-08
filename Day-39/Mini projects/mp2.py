# 2.	Feedback Collector
# A form with Name (Entry), Comments (Text), and a Submit button that displays a thank you message and clears the input.

import tkinter as tk
from tkinter import messagebox
root=tk.Tk()
root.title("Login Form")
root.geometry("500x400")

name_label=tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
name_entry=tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

comments_label=tk.Label(root, text="Comments:")
comments_label.grid(row=1, column=0, padx=10, pady=10, sticky="ne")
comments_text=tk.Text(root, width=30, height=7)
comments_text.grid(row=1, column=1, padx=10, pady=10, sticky="w")

def submit_feedback():
    name=name_entry.get()
    comments=comments_text.get("1.0", tk.END).strip()

    if not name or not comments:
        messagebox.showerror("Error", "Please enter your name & comments.")
        return
    else:
        messagebox.showinfo("Thank you", f"Thank you for your feedback, {name}!")

    name_entry.delete(0, tk.END)
    comments_text.delete("1.0", tk.END)
    
btn=tk.Button(root, text="Submit", command=submit_feedback)
btn .grid(row=2, column=1, padx=10, pady=10)

root.mainloop()