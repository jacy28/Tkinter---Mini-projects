# 🟢 9. Quiz App with Option Selector
# Goal: Conduct a single-question quiz.
# Requirements:
# •	Use Label for question.
# •	Use Combobox or Radiobuttons for options.
# •	Button to check answer.
# •	Label to display correct/wrong.
# •	Layout using grid() in a Frame.

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Quiz App")

frame = tk.Frame(root)
frame.grid(padx=20, pady=20)

question_label = tk.Label(frame, text="What is the capital of France?")
question_label.grid(row=0, column=0, columnspan=2, pady=10)

selected_option = tk.StringVar()

options = ["Berlin", "Madrid", "Paris", "Rome"]
for i, option in enumerate(options):
    tk.Radiobutton(frame, text=option, variable=selected_option, value=option).grid(row=i+1, column=0, sticky="w")

result_var = tk.StringVar()
result_label = tk.Label(frame, textvariable=result_var)
result_label.grid(row=6, column=0, columnspan=2, pady=10)

def check_answer():
    answer = selected_option.get()
    if answer == "Paris":
        result_var.set("Correct!")
    else:
        result_var.set("Wrong!")

check_button = tk.Button(frame, text="Check Answer", command=check_answer)
check_button.grid(row=5, column=0, columnspan=2, pady=5)

root.mainloop()
