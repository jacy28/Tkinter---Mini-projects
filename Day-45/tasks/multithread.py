# # # 1.	Create a simple GUI with a button that starts a long-running function in a separate thread.
# # import tkinter as tk
# # import threading
# # import time
# # root=tk.Tk()
# # root.geometry("300x300")
# # def long_running_task():
# #     print("Task started...")
# #     time.sleep(5) 
# #     print("Task finished!")
# # def start_thread():
# #     thread=threading.Thread(target=long_running_task)
# #     thread.start()
# # btn=tk.Button(root, text="Click Me", command=start_thread)
# # btn.pack(padx=10, pady=10)
# # root.mainloop()

# # # 2.	Show a “Please wait…” message in a label while a thread performs a task.
# # import tkinter as tk
# # import threading
# # import time
# # root=tk.Tk()
# # root.geometry("300x300")
# # def long_task(label):
# #     time.sleep(5)
# #     label.config(text="task Completed")
# # def start_task(label):
# #     label.config(text="Please Wait...")
# #     thread=threading.Thread(target=long_task, args=(label,))
# #     thread.start()
# # label=tk.Label(root, text="Start text")
# # label.pack(pady=10)
# # btn=tk.Button(root, text="Click", command=lambda: start_task(label))
# # btn.pack(pady=10)
# # root.mainloop()

# # # 3.	Use after() to update a label with text fetched from a thread.
# # import tkinter as tk
# # import threading
# # import time
# # root=tk.Tk()
# # root.geometry("300x300")
# # def update_label():
# #     label.config(text="Updated from another thread.")
# # def worker_thread():
# #     time.sleep(2)
# #     root.after(0, update_label)
# # label=tk.Label(root, text="Original text")
# # label.pack(pady=10)
# # btn=tk.Button(root, text="Click", command=lambda: threading.Thread(target=worker_thread).start())
# # btn.pack(pady=10)
# # root.mainloop()

# # # 4.	Run a countdown timer in the background thread and update the GUI label in real time.
# # import tkinter as tk
# # import threading
# # import time
# # root=tk.Tk()
# # root.geometry("300x300")
# # def countdown(label, seconds):
# #     for i in range(seconds, -1, -1):
# #         # Use .after to schedule GUI update in the main thread
# #         label.after(0, lambda i=i: label.config(text=f"Time left: {i} seconds"))
# #         time.sleep(1)
# #     label.after(0, lambda: label.config(text="Time's up!"))

# # def start_countdown(label, seconds):
# #     thread = threading.Thread(target=countdown, args=(label, seconds))
# #     thread.start()

# # label = tk.Label(root, text="Click to start countdown", font=("Arial", 14))
# # label.pack(pady=20)

# # button = tk.Button(root, text="Start Countdown", command=lambda: start_countdown(label, 10))
# # button.pack()
# # root.mainloop()

# # 5.	Display progress updates every second from a thread using after().
# import tkinter as tk
# import threading
# import time
# progress = 0
# running = False
# def update_progress():
#     global progress
#     label.config(text=f"Progress: {progress}%")
#     if progress >= 100:
#         label.config(text="Done!")
# def run_progress():
#     global progress, running
#     while progress < 100 and running:
#         time.sleep(1)
#         progress += 10
#         root.after(0, update_progress)
#     running = False
# def start_thread():
#     global running
#     if not running:
#         running = True
#         threading.Thread(target=run_progress, daemon=True).start()

# root = tk.Tk()
# root.title("Progress Update")
# label = tk.Label(root, text="Progress: 0%")
# label.pack(pady=20)
# button = tk.Button(root, text="Start", command=start_thread)
# button.pack()

# root.mainloop()

# # # 6.	Create a thread that downloads a file (simulated with sleep) and updates progress.
# # import tkinter as tk
# # import threading
# # import time

# # def simulate_download():
# #     global downloading
# #     downloading = True
# #     progress = 0
# #     while progress <= 100 and downloading:
# #         time.sleep(0.5)
# #         progress += 10
# #         root.after(0, lambda p=progress: label.config(text=f"Downloading... {p}%"))
# #     if downloading:
# #         root.after(0, lambda: label.config(text="Download Complete"))

# # def start_download():
# #     threading.Thread(target=simulate_download, daemon=True).start()

# # root = tk.Tk()
# # label = tk.Label(root, text="Ready")
# # label.pack()
# # tk.Button(root, text="Download", command=start_download).pack()

# # root.mainloop()


# # # 7.	Implement a cancelable task with a Stop button that disables the worker thread (use flag).
# # import tkinter as tk 
# # import threading
# # import time
# # running = False

# # def cancellable_task():
# #     global running
# #     running = True
# #     progress = 0
# #     while progress <= 100 and running:
# #         time.sleep(0.5)
# #         progress += 10
# #         root.after(0, lambda p=progress: label.config(text=f"Progress: {p}%"))
# #     if not running:
# #         root.after(0, lambda: label.config(text="Cancelled"))
# #     else:
# #         root.after(0, lambda: label.config(text="Completed"))

# # def start_task():
# #     threading.Thread(target=cancellable_task, daemon=True).start()

# # def stop_task():
# #     global running
# #     running = False

# # root = tk.Tk()
# # label = tk.Label(root, text="Idle")
# # label.pack()
# # tk.Button(root, text="Start", command=start_task).pack()
# # tk.Button(root, text="Stop", command=stop_task).pack()
# # root.mainloop()


# # # 8.	Use threading to simulate API data fetching and show data on GUI safely.
# # import tkinter as tk
# # import threading
# # import time
# # def fetch_api_data():
# #     time.sleep(2)  # simulate delay
# #     data = "Data from API"
# #     root.after(0, lambda: label.config(text=data))

# # def start_fetch():
# #     threading.Thread(target=fetch_api_data, daemon=True).start()

# # root = tk.Tk()
# # label = tk.Label(root, text="Waiting for data...")
# # label.pack()
# # tk.Button(root, text="Fetch", command=start_fetch).pack()
# # root.mainloop()

# # # 9.	Build a progress bar (custom or ttk) that updates as a thread completes its steps.
# # import tkinter as tk
# # import threading
# # import time
# # from tkinter import ttk

# # def update_progressbar():
# #     progress = 0
# #     while progress <= 100:
# #         time.sleep(0.5)
# #         current = progress  # capture current value
# #         root.after(0, set_progress, current)
# #         progress += 10

# # def set_progress(value):
# #     progressbar["value"] = value

# # def start_progressbar():
# #     threading.Thread(target=update_progressbar, daemon=True).start()

# # root = tk.Tk()
# # root.title("Progress Bar Example")

# # progressbar = ttk.Progressbar(root, length=200, maximum=100, mode='determinate')
# # progressbar.pack(pady=10)

# # tk.Button(root, text="Start", command=start_progressbar).pack(pady=5)

# # root.mainloop()

# # # 10.	Animate a label (changing text or color) using a background thread + after().
# # import tkinter as tk
# # import threading
# # import time
# # colors = ["red", "blue", "green", "orange"]

# # def animate_label():
# #     idx = 0
# #     while True:
# #         time.sleep(0.5)
# #         root.after(0, lambda i=idx: label.config(fg=colors[i % len(colors)]))
# #         idx += 1

# # root = tk.Tk()
# # label = tk.Label(root, text="Animated Label", font=("Arial", 18))
# # label.pack()
# # threading.Thread(target=animate_label, daemon=True).start()
# # root.mainloop()


# # # 11.	Handle UI freezing by comparing direct thread UI update (wrong) vs after() (correct).
# # import tkinter as tk
# # import threading
# # import time
# # def wrong_ui_update():
# #     for i in range(5):
# #         time.sleep(1)
# #         label.config(text=f"Step {i}")  # This will freeze UI

# # def correct_ui_update():
# #     def task():
# #         for i in range(5):
# #             time.sleep(1)
# #             root.after(0, lambda i=i: label.config(text=f"Step {i}"))
# #     threading.Thread(target=task, daemon=True).start()

# # root = tk.Tk()
# # label = tk.Label(root, text="Press a button")
# # label.pack()
# # tk.Button(root, text="Wrong", command=wrong_ui_update).pack()
# # tk.Button(root, text="Correct", command=correct_ui_update).pack()
# # root.mainloop()


# # # 12.	Log thread status messages to a Text widget in real-time using after().
# # import tkinter as tk
# # import threading
# # import time
# # def log_status():
# #     for i in range(5):
# #         msg = f"Log line {i}\n"
# #         time.sleep(1)
# #         root.after(0, lambda m=msg: text.insert(tk.END, m))

# # def start_log():
# #     threading.Thread(target=log_status, daemon=True).start()

# # root = tk.Tk()
# # text = tk.Text(root, height=10, width=40)
# # text.pack()
# # tk.Button(root, text="Start Logging", command=start_log).pack()
# # root.mainloop()


# # # 13.	Display loading animation while a background task runs.
# # import tkinter as tk
# # import threading
# # import time
# # def loading_animation():
# #     dots = 0
# #     while running:
# #         dots = (dots + 1) % 4
# #         root.after(0, lambda d=dots: label.config(text="Loading" + "." * d))
# #         time.sleep(0.5)

# # def start_loading_task():
# #     global running
# #     running = True
# #     threading.Thread(target=loading_animation, daemon=True).start()
# #     threading.Thread(target=long_task, daemon=True).start()

# # def long_task():
# #     time.sleep(5)
# #     global running
# #     running = False
# #     root.after(0, lambda: label.config(text="Done!"))

# # root = tk.Tk()
# # label = tk.Label(root, text="Idle")
# # label.pack()
# # tk.Button(root, text="Start", command=start_loading_task).pack()
# # root.mainloop()


# # # 14.	Use threading.Thread with lambda function to run a delay and update status label.
# # import tkinter as tk
# # import threading
# # import time
# # def delayed_status():
# #     time.sleep(3)
# #     root.after(0, lambda: label.config(text="Updated after delay"))

# # tk_root = tk.Tk()
# # label = tk.Label(tk_root, text="Waiting...")
# # label.pack()
# # tk.Button(tk_root, text="Run", command=lambda: threading.Thread(target=delayed_status, daemon=True).start()).pack()
# # tk_root.mainloop()


# # # 15.	Create a multithreaded GUI where each button click starts a separate, independent task.
# # import tkinter as tk
# # import threading
# # import time
# # def task(n):
# #     for i in range(5):
# #         time.sleep(1)
# #         root.after(0, lambda i=i, n=n: text.insert(tk.END, f"Task {n} step {i}\n"))

# # def start_task(n):
# #     threading.Thread(target=task, args=(n,), daemon=True).start()

# # root = tk.Tk()
# # text = tk.Text(root, height=10, width=40)
# # text.pack()
# # for i in range(3):
# #     tk.Button(root, text=f"Start Task {i}", command=lambda n=i: start_task(n)).pack()
# # root.mainloop()
