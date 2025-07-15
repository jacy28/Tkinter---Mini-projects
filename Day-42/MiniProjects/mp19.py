# 🔷 19. Live Scoreboard
# Widgets Used: Canvas, Spinbox, Combobox
# Requirements:
# •	Team A & Team B score via Spinboxes.
# •	Canvas shows scoreboard UI.
# •	Combobox to change team names.
# •	Update scores dynamically.
# •	"Reset Scores" button.

import tkinter as tk
from tkinter import ttk

# --- Functions ---

def update_scoreboard():
    team_a = team_a_name.get()
    team_b = team_b_name.get()
    score_a = int(score_a_spin.get())
    score_b = int(score_b_spin.get())

    canvas.delete("all")
    canvas.create_rectangle(50, 50, 450, 250, fill="black")

    canvas.create_text(150, 100, text=team_a, fill="white", font=("Arial", 16, "bold"))
    canvas.create_text(150, 160, text=str(score_a), fill="cyan", font=("Arial", 32, "bold"))

    canvas.create_text(350, 100, text=team_b, fill="white", font=("Arial", 16, "bold"))
    canvas.create_text(350, 160, text=str(score_b), fill="orange", font=("Arial", 32, "bold"))

def reset_scores():
    score_a_spin.delete(0, tk.END)
    score_a_spin.insert(0, 0)
    score_b_spin.delete(0, tk.END)
    score_b_spin.insert(0, 0)

    team_a_name.set("Team A")
    team_b_name.set("Team B")

    update_scoreboard()

# --- Main Window ---
root = tk.Tk()
root.title("🔷 Live Scoreboard")
root.geometry("500x400")

# --- Canvas ---
canvas = tk.Canvas(root, width=500, height=250, bg="white")
canvas.pack(pady=10)

# --- Controls Frame ---
control_frame = tk.Frame(root)
control_frame.pack(pady=10)

# Team A Controls
tk.Label(control_frame, text="Team A:").grid(row=0, column=0, padx=5)
team_a_name = ttk.Combobox(control_frame, values=["Team A", "Lions", "Tigers", "Eagles"], width=10, state="readonly")
team_a_name.set("Team A")
team_a_name.grid(row=0, column=1, padx=5)

score_a_spin = tk.Spinbox(control_frame, from_=0, to=1000, width=5, command=update_scoreboard)
score_a_spin.grid(row=0, column=2, padx=5)

# Team B Controls
tk.Label(control_frame, text="Team B:").grid(row=1, column=0, padx=5)
team_b_name = ttk.Combobox(control_frame, values=["Team B", "Sharks", "Panthers", "Wolves"], width=10, state="readonly")
team_b_name.set("Team B")
team_b_name.grid(row=1, column=1, padx=5)

score_b_spin = tk.Spinbox(control_frame, from_=0, to=1000, width=5, command=update_scoreboard)
score_b_spin.grid(row=1, column=2, padx=5)

# --- Reset Button ---
tk.Button(root, text="🔁 Reset Scores", command=reset_scores).pack(pady=10)

# --- Event Bindings for Live Update ---
team_a_name.bind("<<ComboboxSelected>>", lambda e: update_scoreboard())
team_b_name.bind("<<ComboboxSelected>>", lambda e: update_scoreboard())
score_a_spin.bind("<KeyRelease>", lambda e: update_scoreboard())
score_b_spin.bind("<KeyRelease>", lambda e: update_scoreboard())

# Initial draw
update_scoreboard()

root.mainloop()
