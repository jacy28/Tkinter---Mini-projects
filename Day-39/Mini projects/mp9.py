# 9.	Guess the Number Game
#	Entry for user guess, Button to submit, Label for hints (too high/low/correct), and a reset Button.

import tkinter as tk
from tkinter import messagebox
import random

# Generate random number
secret_number = random.randint(1, 100)

def check_guess():
    try:
        guess = int(guess_entry.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a number between 1 and 100.")
        return

    if guess < 1 or guess > 100:
        messagebox.showwarning("Out of range", "Number must be between 1 and 100.")
    elif guess < secret_number:
        result_label.config(text="Too low! Try again.")
    elif guess > secret_number:
        result_label.config(text="Too high! Try again.")
    else:
        result_label.config(text="🎉 Correct! You guessed it!")

def reset_game():
    global secret_number
    secret_number = random.randint(1, 100)
    guess_entry.delete(0, tk.END)
    result_label.config(text="New game started! Guess a number.")

# GUI Setup
root = tk.Tk()
root.title("Guess the Number")
root.geometry("400x250")

tk.Label(root, text="Guess a number between 1 and 100").pack(pady=10)

guess_entry = tk.Entry(root, width=20)
guess_entry.pack()

check_button = tk.Button(root, text="Submit Guess", command=check_guess)
check_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

reset_button = tk.Button(root, text="Reset Game", command=reset_game)
reset_button.pack(pady=5)

root.mainloop()
