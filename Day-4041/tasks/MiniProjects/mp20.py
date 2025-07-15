# 📂 20. File Name Generator
# Goal: Generate file names from form data.
# Requirements:
# •	Fields: Project name, Date, Type.
# •	Combine and generate name like project_2025-07-02_type.txt.
# •	Display in Label.
# •	Copy to clipboard using clipboard_append().


import tkinter as tk

def generate_filename():
    project = project_entry.get().strip()
    date = date_entry.get().strip()
    file_type = type_entry.get().strip()

    if not project or not date or not file_type:
        result_label.config(text="All fields are required!", fg="red")
        return

    filename = f"{project}_{date}_{file_type}.txt"
    result_label.config(text=f"Generated: {filename}", fg="green")
    root.clipboard_clear()
    root.clipboard_append(filename)

# --- GUI Setup ---
root = tk.Tk()
root.title("📂 File Name Generator")
root.geometry("400x250")

# Labels and Entries
tk.Label(root, text="Project Name:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
project_entry = tk.Entry(root, width=30)
project_entry.grid(row=0, column=1)

tk.Label(root, text="Date (YYYY-MM-DD):").grid(row=1, column=0, padx=10, pady=10, sticky="e")
date_entry = tk.Entry(root, width=30)
date_entry.grid(row=1, column=1)

tk.Label(root, text="File Type:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
type_entry = tk.Entry(root, width=30)
type_entry.grid(row=2, column=1)

# Generate Button
generate_btn = tk.Button(root, text="Generate File Name", command=generate_filename)
generate_btn.grid(row=3, column=0, columnspan=2, pady=15)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 10, "bold"))
result_label.grid(row=4, column=0, columnspan=2, pady=5)

root.mainloop()
