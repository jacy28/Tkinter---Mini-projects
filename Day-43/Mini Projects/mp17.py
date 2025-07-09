# ✅ 17. Quiz App with Dialogs
# Objective: Run a quiz and confirm answers via dialog.
# Requirements:
# •	Frame for question and options.
# •	Menu: Quiz > Start New, End.
# •	On submit, use messagebox.askyesno() to confirm answer.
# •	Use Toplevel() to display final score.

import tkinter as tk
from tkinter import messagebox

# Quiz data
questions = [
    {"q": "What is the capital of France?", "options": ["Paris", "Rome", "Berlin", "Madrid"], "answer": "Paris"},
    {"q": "2 + 2 = ?", "options": ["3", "4", "5", "6"], "answer": "4"},
    {"q": "Which language is this app written in?", "options": ["Python", "Java", "C++", "Ruby"], "answer": "Python"}
]

current_index = 0
score = 0

def start_quiz():
    global current_index, score
    current_index = 0
    score = 0
    show_question()

def show_question():
    if current_index >= len(questions):
        show_score()
        return

    question_data = questions[current_index]
    question_label.config(text=question_data["q"])

    for i, option in enumerate(question_data["options"]):
        option_buttons[i].config(text=option, value=option)

def submit_answer():
    global current_index, score
    selected = selected_option.get()
    if not selected:
        messagebox.showwarning("No Selection", "Please choose an option.")
        return

    confirm = messagebox.askyesno("Confirm", f"Are you sure '{selected}' is your final answer?")
    if confirm:
        if selected == questions[current_index]["answer"]:
            score += 1
        current_index += 1
        selected_option.set(None)
        show_question()

def show_score():
    top = tk.Toplevel(root)
    top.title("Quiz Result")
    tk.Label(top, text=f"Your Score: {score}/{len(questions)}", font=("Arial", 14)).pack(padx=20, pady=20)
    tk.Button(top, text="Close", command=top.destroy).pack(pady=10)

def exit_quiz():
    root.quit()

root = tk.Tk()
root.title("Quiz App")
root.geometry("400x300")

# Menu bar
menu_bar = tk.Menu(root)
quiz_menu = tk.Menu(menu_bar, tearoff=0)
quiz_menu.add_command(label="Start New", command=start_quiz)
quiz_menu.add_command(label="End", command=exit_quiz)
menu_bar.add_cascade(label="Quiz", menu=quiz_menu)
root.config(menu=menu_bar)

# Question frame
frame = tk.Frame(root)
frame.pack(pady=20)

question_label = tk.Label(frame, text="", font=("Arial", 12), wraplength=300)
question_label.pack(pady=10)

selected_option = tk.StringVar()
option_buttons = []
for _ in range(4):
    rb = tk.Radiobutton(frame, text="", variable=selected_option, value="", font=("Arial", 10))
    rb.pack(anchor="w")
    option_buttons.append(rb)

tk.Button(root, text="Submit Answer", command=submit_answer).pack(pady=10)

start_quiz()
root.mainloop()
