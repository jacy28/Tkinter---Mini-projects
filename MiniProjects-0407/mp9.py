# 9. Quiz Application
# Objective: Conduct a 5-question quiz.
# Features:
# •	Questions displayed using Label, options via Radiobuttons.
# •	Layout using grid().
# •	Score shown at the end.
# •	Disable inputs after each question.
# •	Use Button to navigate next question.

import tkinter as tk
from tkinter import messagebox

quiz_data = [
    {"q": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Rome"], "answer": "Paris"},
    {"q": "2 + 2 = ?", "options": ["3", "4", "5", "2"], "answer": "4"},
    {"q": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Venus"], "answer": "Mars"},
    {"q": "Which language is this quiz written in?", "options": ["Python", "Java", "C++", "HTML"], "answer": "Python"},
    {"q": "What is the boiling point of water?", "options": ["90°C", "100°C", "110°C", "120°C"], "answer": "100°C"}
]

current_q = 0
score = 0

def load_question():
    q_label.config(text=quiz_data[current_q]["q"])
    for i, opt in enumerate(quiz_data[current_q]["options"]):
        radio_btns[i].config(text=opt, value=opt, state="normal")
    next_btn.config(state="disabled")
    selected.set(None)

def check_answer():
    global score
    user_ans = selected.get()
    if not user_ans:
        messagebox.showwarning("No Selection", "Please select an option.")
        return
    correct_ans = quiz_data[current_q]["answer"]
    if user_ans == correct_ans:
        score += 1
    for rb in radio_btns:
        rb.config(state="disabled")
    next_btn.config(state="normal")

def next_question():
    global current_q
    current_q += 1
    if current_q < len(quiz_data):
        load_question()
    else:
        show_result()

def show_result():
    q_label.config(text=f"Quiz Complete! Your score: {score} / {len(quiz_data)}")
    for rb in radio_btns:
        rb.grid_remove()
    submit_btn.grid_remove()
    next_btn.grid_remove()

root = tk.Tk()
root.title("Quiz App")
root.geometry("400x300")

selected = tk.StringVar()

q_label = tk.Label(root, text="", font=("Arial", 14), wraplength=350, justify="left")
q_label.grid(row=0, column=0, columnspan=2, pady=20)

radio_btns = []
for i in range(4):
    rb = tk.Radiobutton(root, text="", variable=selected, value="", font=("Arial", 12), anchor="w", justify="left", command=check_answer)
    rb.grid(row=i+1, column=0, sticky="w", padx=20, pady=2)
    radio_btns.append(rb)

submit_btn = tk.Button(root, text="Submit", command=check_answer)
submit_btn.grid(row=6, column=0, pady=10)

next_btn = tk.Button(root, text="Next", command=next_question, state="disabled")
next_btn.grid(row=6, column=1, pady=10)

load_question()

root.mainloop()
