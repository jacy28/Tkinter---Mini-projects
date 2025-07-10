# ✅ 20. Emoji Reaction Panel (Custom Widget)
# Objective: React with emojis using a custom widget class.
# Features:
# •	Class widget with emoji buttons (😀, 😢, 😠, etc.).
# •	Clicking emoji updates a Label or prints to console.
# •	Allow multiple instances of emoji bar on different messages.

import tkinter as tk

class EmojiReactor(tk.Frame):
    def __init__(self, master, label_target=None, **kwargs):
        super().__init__(master, **kwargs)
        self.label_target = label_target
        for emoji in ["😀", "😢", "😠", "❤️"]:
            tk.Button(self, text=emoji, font=("Arial", 14), command=lambda e=emoji: self.react(e)).pack(side="left", padx=2)

    def react(self, emoji):
        if self.label_target:
            self.label_target.config(text=f"Reaction: {emoji}")
        else:
            print(f"Reacted with: {emoji}")

root = tk.Tk()
root.geometry("300x200")

msg1 = tk.Label(root, text="Message 1", font=("Arial", 12))
msg1.pack()
reaction1 = tk.Label(root, text="")
reaction1.pack()
EmojiReactor(root, reaction1).pack(pady=5)

msg2 = tk.Label(root, text="Message 2", font=("Arial", 12))
msg2.pack()
reaction2 = tk.Label(root, text="")
reaction2.pack()
EmojiReactor(root, reaction2).pack(pady=5)

root.mainloop()
