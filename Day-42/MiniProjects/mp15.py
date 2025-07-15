# 🔷 15. Fitness Repetition Counter
# Widgets Used: Spinbox, Canvas, Button
# Requirements:
# •	Use Spinbox to set number of reps (e.g., jumping jacks).
# •	Canvas shows a stick figure.
# •	Animate jumping motion with each repetition.
# •	Button to start/stop.
# •	Display current count on canvas.
import tkinter as tk

root = tk.Tk()
root.title("🔷 Fitness Repetition Counter")
root.geometry("500x500")

# --- Global State ---
is_animating = False
current_rep = 0
max_reps = 0
stick_parts = {}

# --- Create Canvas ---
canvas = tk.Canvas(root, width=400, height=350, bg="white")
canvas.pack(pady=10)

# --- Stick Figure Drawing ---
def draw_stick_figure(jump=False):
    canvas.delete("stick")
    x, y = 200, 180
    arm_offset = 30 if not jump else 50
    leg_offset = 30 if not jump else 50
    arm_y = y + 30 if not jump else y + 10

    # Head
    canvas.create_oval(x-15, y-60, x+15, y-30, fill="lightblue", tags="stick")

    # Body
    canvas.create_line(x, y-30, x, y+30, width=4, tags="stick")

    # Arms
    canvas.create_line(x, y, x - arm_offset, arm_y, width=3, tags="stick")
    canvas.create_line(x, y, x + arm_offset, arm_y, width=3, tags="stick")

    # Legs
    canvas.create_line(x, y+30, x - leg_offset, y+70, width=3, tags="stick")
    canvas.create_line(x, y+30, x + leg_offset, y+70, width=3, tags="stick")

    # Counter Text
    canvas.create_text(200, 20, text=f"Reps: {current_rep}/{max_reps}", font=("Arial", 16), tags="stick")

# --- Animation Logic ---
def animate():
    global current_rep, is_animating
    if not is_animating or current_rep >= max_reps:
        is_animating = False
        return

    draw_stick_figure(jump=True)
    root.after(300, lambda: draw_stick_figure(jump=False))
    current_rep += 1
    root.after(600, animate)  # Wait before next jump

def start_animation():
    global is_animating, current_rep, max_reps
    if not is_animating:
        max_reps = int(rep_spin.get())
        current_rep = 0
        is_animating = True
        animate()

def stop_animation():
    global is_animating
    is_animating = False

# --- Controls ---
control_frame = tk.Frame(root)
control_frame.pack(pady=10)

tk.Label(control_frame, text="Set Reps:").grid(row=0, column=0, padx=5)
rep_spin = tk.Spinbox(control_frame, from_=1, to=50, width=5)
rep_spin.grid(row=0, column=1, padx=5)

tk.Button(control_frame, text="Start", command=start_animation).grid(row=0, column=2, padx=10)
tk.Button(control_frame, text="Stop", command=stop_animation).grid(row=0, column=3, padx=10)

# --- Initial Draw ---
draw_stick_figure()

root.mainloop()
