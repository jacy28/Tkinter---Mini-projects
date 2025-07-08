# 15.	Basic Quiz App
# 	Label for question, Entry for answer, Button to submit, and Label to show if the answer is correct or not.

import tkinter as tk
from tkinter import messagebox

# Sample quiz data
question = "What is the capital of France?"
correct_answer = "Paris"

# Function to check answer
def check_answer():
    user_answer = answer_entry.get().strip()
    if user_answer.lower() == correct_answer.lower():
        result_label.config(text="✅ Correct!", fg="green")
    else:
        result_label.config(text="❌ Incorrect. Try again.", fg="red")

# Main window
root = tk.Tk()
root.title("Quiz App")
root.geometry("400x250")

# Question Label
question_label = tk.Label(root, text=question, font=("Arial", 14))
question_label.pack(pady=20)

# Entry for Answer
answer_entry = tk.Entry(root, font=("Arial", 12), width=30)
answer_entry.pack(pady=5)

# Submit Button
submit_btn = tk.Button(root, text="Submit Answer", command=check_answer)
submit_btn.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
