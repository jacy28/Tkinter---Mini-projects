# 📓 12. Simple Diary App
# Goal: Save daily notes with date stamp.
# Requirements:
# •	Text widget for notes.
# •	Button to save notes to file named with current date.
# •	Label to show "Note saved".
# •	Use place() or grid().

import tkinter as tk
from datetime import datetime

# --- Save note function ---
def save_note():
    content = text_area.get("1.0", tk.END).strip()
    if content:
        date_str = datetime.now().strftime("%Y-%m-%d")
        filename = f"note_{date_str}.txt"
        with open(filename, "w") as f:
            f.write(content)
        status_label.config(text="✅ Note saved!", fg="green")
    else:
        status_label.config(text="⚠️ Note is empty.", fg="red")

# --- GUI Setup ---
root = tk.Tk()
root.title("📓 Simple Diary")
root.geometry("400x300")

# --- Text Widget for Notes ---
text_area = tk.Text(root, height=10, width=40)
text_area.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# --- Save Button ---
save_button = tk.Button(root, text="Save Note", command=save_note)
save_button.grid(row=1, column=0, padx=10, pady=10)

# --- Status Label ---
status_label = tk.Label(root, text="", font=("Arial", 10))
status_label.grid(row=1, column=1, padx=10, pady=10)

root.mainloop()
