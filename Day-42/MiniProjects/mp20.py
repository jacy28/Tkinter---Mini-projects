# 🔷 20. Interactive Calendar Picker
# Widgets Used: Combobox, Spinbox, Canvas
# Requirements:
# •	Combobox for month selection.
# •	Spinbox for year.
# •	Canvas to display calendar (7x6 grid).
# •	Highlight current day.
# •	On clicking a date, display info in Label (like events or notes).

import tkinter as tk
from tkinter import ttk
import calendar
from datetime import datetime

# --- Functions ---

def draw_calendar():
    canvas.delete("all")
    
    month = month_combo.current() + 1
    year = int(year_spin.get())
    cal = calendar.monthcalendar(year, month)

    # Draw header
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    for i, day in enumerate(days):
        canvas.create_text(50 + i*60, 20, text=day, font=("Arial", 10, "bold"))

    today = datetime.today()
    for row, week in enumerate(cal):
        for col, day in enumerate(week):
            x = 20 + col * 60
            y = 40 + row * 40
            if day != 0:
                rect = canvas.create_rectangle(x, y, x+50, y+30, fill="white", outline="gray")

                # Highlight today
                if day == today.day and month == today.month and year == today.year:
                    canvas.itemconfig(rect, fill="lightblue")

                text_id = canvas.create_text(x+25, y+15, text=str(day), font=("Arial", 10))
                # Store day-cell info for event binding
                canvas.tag_bind(text_id, "<Button-1>", lambda e, d=day: show_day_info(d))

def show_day_info(day):
    month = month_combo.get()
    year = year_spin.get()
    info_label.config(text=f"📅 You selected: {day} {month}, {year}")

def refresh_calendar(*args):
    draw_calendar()

# --- Main Window ---
root = tk.Tk()
root.title("🔷 Interactive Calendar Picker")
root.geometry("500x400")

# --- Controls Frame ---
control_frame = tk.Frame(root)
control_frame.pack(pady=10)

tk.Label(control_frame, text="Month:").grid(row=0, column=0, padx=5)
month_combo = ttk.Combobox(control_frame, values=list(calendar.month_name)[1:], width=10, state="readonly")
month_combo.grid(row=0, column=1, padx=5)
month_combo.current(datetime.today().month - 1)

tk.Label(control_frame, text="Year:").grid(row=0, column=2, padx=5)
year_spin = tk.Spinbox(control_frame, from_=1900, to=2100, width=6)
year_spin.grid(row=0, column=3, padx=5)
year_spin.delete(0, tk.END)
year_spin.insert(0, datetime.today().year)

# --- Canvas for calendar ---
canvas = tk.Canvas(root, width=480, height=300, bg="white")
canvas.pack(pady=10)

# --- Info Label ---
info_label = tk.Label(root, text="🛈 Click a date to see details", font=("Arial", 10))
info_label.pack()

# --- Event bindings ---
month_combo.bind("<<ComboboxSelected>>", refresh_calendar)
year_spin.bind("<KeyRelease>", refresh_calendar)

# Initial draw
draw_calendar()

root.mainloop()
