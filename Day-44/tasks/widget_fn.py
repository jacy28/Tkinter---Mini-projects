# # 46.	Create a label that changes color when clicked using a bound event.
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# label=tk.Label(root, text="Bound Event Ex")
# label.pack(padx=20, pady=20)
# def change_color(event):
#     label.config(fg="green")
# label.bind("<Button-1>", change_color)
# root.mainloop()

# # 47.	Dynamically resize a widget (e.g., label font increases) on mouse hover.
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# label=tk.Label(root, text="Bound Event Ex", font=("Arial", 14))
# label.pack(padx=20, pady=20)
# def on_enter(event):
#     label.config(font=("Arial", 18))
# def on_leave(event):
#     label.config(font=("Arial", 14))
# label.bind("<Enter>", on_enter)
# label.bind("<Leave>", on_leave)
# root.mainloop()

# # 48.	Create a custom "Password Entry" that toggles visibility on button click.
# import tkinter as tk
# root = tk.Tk()
# root.geometry("300x300")
# pw_label=tk.Label(root, text="Password:")
# pw_label.pack(pady=10)
# password_entry = tk.Entry(root, show="*")
# password_entry.pack(pady=5)
# def toggle_password():
#     if password_entry.cget('show') == '':
#         password_entry.config(show='*')
#         toggle_btn.config(text='Show')
#     else:
#         password_entry.config(show='')
#         toggle_btn.config(text='Hide')
# toggle_btn = tk.Button(root, text="Show", command=toggle_password)
# toggle_btn.pack(pady=10)
# root.mainloop()

# # 49.	Make a progress tracker: Each button click fills a new character in a label.
# import tkinter as tk
# root = tk.Tk()
# root.geometry("300x300")
# progress = ""
# goal = 10  # total steps
# progress_label = tk.Label(root, text="_" * goal, font=("Arial", 16))
# progress_label.pack(pady=20)
# def update_progress():
#     global progress
#     if len(progress) < goal:
#         progress += "#"
#         updated = progress + "_" * (goal - len(progress))
#         progress_label.config(text=updated)
#     else:
#         btn.config(state="disabled")
# btn = tk.Button(root, text="Next", command=update_progress)
# btn.pack(pady=10)
# root.mainloop()

# # 50.	Build a real-time character counter widget for a text input field.
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# text=tk.Text(root, width=20, height=5)
# text.pack(padx=10, pady=10)
# counter_label=tk.Label(root, text="Charaters count: 0")
# counter_label.pack(padx=10, pady=20)
# def update_count(event):
#     content=text.get("1.0", "end-1c")
#     counter_label.config(text=f"Characters count: {len(content)}")
# text.bind("<KeyRelease>", update_count)
# root.mainloop()