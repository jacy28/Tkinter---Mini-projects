# 🔷 11. Scrolling News Reader
# Widgets Used: Listbox, Scrollbar, Button
# Requirements:
# •	Listbox displays a list of news headlines (20+).
# •	Scrollbar for navigation.
# •	Click a headline to open details in a popup.
# •	Refresh button to simulate new headlines.
# •	Auto-scroll feature (like ticker) using after() method.

import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.title("🔷 Scrolling News Reader")
root.geometry("400x400")

# Sample news pool
news_pool = [
    "Breaking: Market hits all-time high!",
    "Sports: Local team wins championship",
    "Weather: Heavy rain expected tomorrow",
    "Politics: Election debates heat up",
    "Health: New research on sleep patterns",
    "Tech: AI revolutionizes industry",
    "Travel: Top destinations for 2025",
    "Education: Online courses rise in popularity",
    "Entertainment: Upcoming movie releases",
    "Science: Mars mission milestone reached",
    "Finance: Tips to save money",
    "World: Peace talks continue",
    "Environment: Forests recovering slowly",
    "Business: Startup culture booming",
    "Crime: Major bust in downtown area",
    "Food: Top 10 trending recipes",
    "Fashion: Summer trends unveiled",
    "Gaming: New console announced",
    "Auto: Electric vehicles gain traction",
    "History: Rare artifact discovered"
]

# Add news to listbox
def load_news():
    listbox.delete(0, tk.END)
    headlines = random.sample(news_pool, len(news_pool))  # Shuffle
    for item in headlines:
        listbox.insert(tk.END, item)

# Show popup on click
def show_details(event):
    selected = listbox.curselection()
    if selected:
        title = listbox.get(selected[0])
        messagebox.showinfo("News Details", f"Details for:\n\n{title}")

# Auto scroll
def auto_scroll():
    if auto_scroll_enabled.get():
        if listbox.size() > 1:
            first = listbox.get(0)
            listbox.delete(0)
            listbox.insert(tk.END, first)
        root.after(2000, auto_scroll)  # adjust speed here

# Toggle auto-scroll
def toggle_scroll():
    if auto_scroll_enabled.get():
        auto_scroll()
        
# === UI Elements === #
frame = tk.Frame(root)
frame.pack(pady=10, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set, height=15)
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=listbox.yview)

listbox.bind("<<ListboxSelect>>", show_details)

# Refresh button
tk.Button(root, text="🔁 Refresh Headlines", command=load_news).pack(pady=5)

# Auto-scroll toggle
auto_scroll_enabled = tk.BooleanVar()
tk.Checkbutton(root, text="Auto Scroll (Ticker)", variable=auto_scroll_enabled, command=toggle_scroll).pack()

# Initial load
load_news()
auto_scroll()  # Start auto scroll if enabled later

root.mainloop()
