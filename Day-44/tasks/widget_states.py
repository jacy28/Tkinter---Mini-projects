# # 1.	Create a button that disables itself when clicked.
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# def disable_btn():
#     btn.config(state="disabled")
# btn=tk.Button(root, text="Click Me", command=disable_btn, padx=5, pady=10)
# btn.pack()
# root.mainloop()

# # 2.	Create a Checkbutton that disables a text input field when selected.
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# def toggle_btn():
#     if check_var.get()==1:
#         entry.config(state="disabled")
#     else:
#         entry.config(state="normal")
# check_var=tk.IntVar()
# entry=tk.Entry(root)
# entry.pack(padx=5, pady=10)
# checkbtn=tk.Checkbutton(root, text="Disbled check button", variable=check_var, command=toggle_btn)
# checkbtn.pack(padx=5, pady=10)
# root.mainloop()


# # 3.	Create two buttons — one disables the other on click.
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# def disable_edit():
#     edit_btn.config(state="disabled")
# edit_btn=tk.Button(root, text="Edit")
# edit_btn.pack(padx=10, pady=10)
# save_btn=tk.Button(root, text="Save", command=disable_edit)
# save_btn.pack(padx=10, pady=10)
# root.mainloop()


# # 4.	Build a form with an initially disabled "Submit" button that becomes enabled when a checkbox is ticked.
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# def enable_btn():
#     if check_var.get()==1:
#         submit_btn.config(state="normal")
#     else:
#         submit_btn.config(state="disabled")
# check_var=tk.IntVar()
# name_label=tk.Label(root, text="Name:")
# name_label.grid(row=0, column=0, padx=5, pady=10)
# name_entry=tk.Entry(root)
# name_entry.grid(row=0, column=1)
# email_label=tk.Label(root, text="Email:")
# email_label.grid(row=1, column=0, padx=5, pady=10)
# email_entry=tk.Entry(root)
# email_entry.grid(row=1, column=1, padx=5, pady=10)
# check_box=tk.Checkbutton(root, text="I agree", variable=check_var, command=enable_btn)
# check_box.grid(row=2, column=1, padx=5, pady=10)
# submit_btn=tk.Button(root, text="Submit", state="disabled")
# submit_btn.grid(row=3, column=1, padx=5, pady=10)
# root.mainloop()

# # 5.	Create a text entry that becomes non-editable (state="disabled") on clicking a button.
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# def disable_entry():
#     name_entry.config(state="disabled")
# name_label=tk.Label(root, text="Name:")
# name_label.grid(row=0, column=0, padx=5, pady=10)
# name_entry=tk.Entry(root)
# name_entry.grid(row=0, column=1)
# btn=tk.Button(root, text="Click", command=disable_entry)
# btn.grid(row=3, column=1, padx=5, pady=10)
# root.mainloop()

# # 6.	Change a button's state from disabled to normal after 5 seconds using after().
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# def change_state():
#     btn.config(state="normal")
# btn=tk.Button(root, text="Click", state="disabled")
# btn.pack(padx=10, pady=10)
# btn.after(5000, change_state)
# root.mainloop()

# # 7.	Display a Label with activeforeground color change on hover.
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# def on_enter(event):
#     label.config(fg="green")
# def on_leave(event):
#     label.config(fg="black")
# label=tk.Label(root, text="Welcome, Tkinter", font=("Arial", 14))
# label.pack(padx=10, pady=10)
# label.bind("<Enter>", on_enter)
# label.bind("<Leave>", on_leave)
# root.mainloop()

# # 8.	Use state="active" on a button and show its effect during mouse hover.
# import tkinter as tk
# root=tk.Tk()
# root.geometry("300x300")
# btn=tk.Button(root, text="Hover Me", bg="pink", fg="black", activeforeground="green", activebackground="white")
# btn.pack(pady=10)
# root.mainloop()

# # 9.	Toggle widget states (enable/disable) using a dropdown (Combobox).
# import tkinter as tk
# from tkinter import ttk
# root=tk.Tk() 
# root.geometry("300x300")
# def toggle_state(event):
#     selection=dropdown.get()
#     if selection=="Enable":
#         btn.config(state="normal")
#     else:
#         btn.config(state="disabled")
# dropdown=ttk.Combobox(root, values=["Enable", "Disable"])
# dropdown.current(0)
# dropdown.pack(padx=10, pady=10)
# dropdown.bind("<<ComboboxSelected>>", toggle_state)
# btn=tk.Button(root, text="Click Me")
# btn.pack(padx=10, pady=10)
# root.mainloop()

# # 10.	Dynamically disable a group of buttons using a loop.
# import tkinter as tk
# from tkinter import ttk
# root=tk.Tk()
# root.geometry("300x300")
# def disable_all():
#     for b in buttons:
#         b.config(state="disabled")
# buttons=[]
# for i in range(5):
#     btn=tk.Button(root, text=f"Button{i+1}")
#     btn.pack(padx=10, pady=10)
#     buttons.append(btn)
# disable_btn=tk.Button(root, text="Disable All", command=disable_all)
# disable_btn.pack(padx=10, pady=10)
# root.mainloop()

# # 11.	Build a reset button that restores all other widgets to their default (normal) state.
# import tkinter as tk
# from tkinter import ttk
# root=tk.Tk()
# root.geometry("300x400")
# def disable_all():
#     for b in buttons:
#         b.config(state="disabled")
# def reset_all():
#     for b in buttons:
#         b.config(state="normal")
# buttons=[]
# for i in range(5):
#     btn=tk.Button(root, text=f"Button{i+1}")
#     btn.pack(padx=10, pady=10)
#     buttons.append(btn)
# disable_btn=tk.Button(root, text="Disable All", command=disable_all)
# disable_btn.pack(padx=10, pady=10)
# reset_btn=tk.Button(root, text="Reset", command=reset_all)
# reset_btn.pack(padx=10, pady=10)
# root.mainloop()

# # 12.	Show visual state change by updating background and foreground based on state.
# import tkinter as tk
# from tkinter import ttk
# root=tk.Tk()
# root.geometry("300x300")
# btn=tk.Button(root, text="Click Me")
# btn.pack(padx=10, pady=10)
# def enable_btn():
#     btn.config(fg="blue", bg="white")
# def disable_btn():
#     btn.config(state="disabled", fg="grey", bg="lightgrey")
# enable_btn=tk.Button(root, text="Enable", command=enable_btn)
# enable_btn.pack(padx=10, pady=10)
# disable_btn=tk.Button(root, text="Disable", command=disable_btn)
# disable_btn.pack(padx=10, pady=10)
# root.mainloop()

# # 13.	Disable a Spinbox input using another widget's action.
# import tkinter as tk
# from tkinter import ttk
# root=tk.Tk()
# root.geometry("300x300")
# def disable_spin():
#     spin.config(state="disabled")
# spin=tk.Spinbox(root, from_=4, to=10)
# spin.pack(padx=10, pady=10)
# btn=tk.Button(root, text="Disable", command=disable_spin)
# btn.pack(padx=10, pady=10)
# root.mainloop()

# # 14.	Make a radio button group where selection disables/unlocks associated controls.
# import tkinter as tk
# root = tk.Tk()
# root.geometry("300x300")
# def toggle_controls():
#     if selected_option.get() == 1:
#         entry.config(state="disabled")
#     else:
#         entry.config(state="normal")
# selected_option = tk.IntVar(value=1)
# radio1 = tk.Radiobutton(root, text="Disable Entry", variable=selected_option, value=1, command=toggle_controls)
# radio1.pack(pady=5)
# radio2 = tk.Radiobutton(root, text="Enable Entry", variable=selected_option, value=2, command=toggle_controls)
# radio2.pack(pady=5)
# entry = tk.Entry(root)
# entry.pack(pady=20)
# toggle_controls()
# root.mainloop()


# # 15.	Combine multiple controls (Entry + Button + Label) and toggle their states simultaneously.
# import tkinter as tk
# from tkinter import ttk
# root=tk.Tk()
# root.geometry("300x300")
# label=tk.Label(root, text="Name:")
# label.grid(row=0, column=0, padx=10, pady=10)
# entry=tk.Entry(root)
# entry.grid(row=0, column=1, padx=10, pady=10)
# btn=tk.Button(root, text="Submit")
# btn.grid(row=1, column=1, pady=20)
# def toggle_all():
#     current_state=entry['state']
#     new_state="disabled" if current_state=="normal" else "normal"
#     entry.config(state=new_state)
#     btn.config(state=new_state)
#     label.config(fg="grey" if new_state == "disabled" else "black")
# toggle_btn=tk.Button(root, text="Toggle btn", command=toggle_all)
# toggle_btn.grid(row=2, column=1, pady=20)
# root.mainloop()