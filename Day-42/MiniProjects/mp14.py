# 🔷 14. Simple Polling App
# Widgets Used: Combobox, Listbox, Scrollbar
# Requirements:
# •	Choose poll question from Combobox.
# •	Listbox to show options.
# •	Allow selection and submit vote.
# •	Show result count next to each option.
# •	Scrollbar if poll options exceed 10.

import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("🔷 Simple Polling App")
root.geometry("400x400")

# --- Poll Data ---
poll_data = {
    "Favorite Programming Language": ["Python", "Java", "C++", "JavaScript", "Rust", "Go", "Swift", "Ruby", "Kotlin", "C#", "PHP"],
    "Best Movie Genre": ["Action", "Comedy", "Drama", "Horror", "Sci-Fi", "Romance", "Documentary", "Fantasy"],
    "Preferred Meal Time": ["Breakfast", "Lunch", "Dinner", "Snacks"]
}

vote_counts = {}

# Initialize vote counts
for question, options in poll_data.items():
    vote_counts[question] = {option: 0 for option in options}

# --- Functions ---

def update_options(event=None):
    listbox.delete(0, tk.END)
    selected_question = question_combo.get()
    options = poll_data.get(selected_question, [])
    for option in options:
        count = vote_counts[selected_question][option]
        listbox.insert(tk.END, f"{option} - {count} votes")

def submit_vote():
    selected_question = question_combo.get()
    if not selected_question:
        messagebox.showwarning("Warning", "Please select a question.")
        return
    try:
        selected_index = listbox.curselection()[0]
        selected_option = listbox.get(selected_index).split(" - ")[0]
        vote_counts[selected_question][selected_option] += 1
        update_options()
        messagebox.showinfo("Thank You!", f"Your vote for '{selected_option}' has been recorded.")
    except IndexError:
        messagebox.showwarning("Warning", "Please select an option to vote.")

# --- Widgets ---

tk.Label(root, text="Select a Poll Question:").pack(pady=5)

question_combo = ttk.Combobox(root, values=list(poll_data.keys()), state="readonly")
question_combo.pack(pady=5)
question_combo.bind("<<ComboboxSelected>>", update_options)

# Frame for Listbox and Scrollbar
frame = tk.Frame(root)
frame.pack(pady=5, expand=True, fill="both")

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set, height=10)
listbox.pack(side="left", fill="both", expand=True)
scrollbar.config(command=listbox.yview)

submit_btn = tk.Button(root, text="Submit Vote", command=submit_vote)
submit_btn.pack(pady=10)

# Set default question
question_combo.set("Favorite Programming Language")
update_options()

root.mainloop()
