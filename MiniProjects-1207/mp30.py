# 50. Language Translator with Text-to-Speech
# •	Input box for source text
# •	Choose language using ttk.Combobox
# •	Translate using Google Translate API
# •	Use pyttsx3 or gTTS to speak text
# •	Save translation history

import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator
import pyttsx3
import json
import time

# Initialize TTS engine
tts_engine = pyttsx3.init()

# History storage
history = []

# Supported languages (simplified list)
languages = {
    "English": "en",
    "Hindi": "hi",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Chinese": "zh-CN",
    "Arabic": "ar",
    "Japanese": "ja",
    "Russian": "ru",
    "Bengali": "bn"
}

# Main Window
root = tk.Tk()
root.title("🈯 Language Translator with Speech")
root.geometry("600x500")

# --- Widgets ---

# Input Text
tk.Label(root, text="Enter Text:", font=("Arial", 12)).pack(pady=5)
input_text = tk.Text(root, height=5, font=("Arial", 12))
input_text.pack(padx=10, pady=5, fill=tk.X)

# Language Selection
frame = tk.Frame(root)
frame.pack(pady=5)

tk.Label(frame, text="From:", font=("Arial", 11)).grid(row=0, column=0, padx=5)
src_lang = ttk.Combobox(frame, values=list(languages.keys()), width=15, state="readonly")
src_lang.set("English")
src_lang.grid(row=0, column=1, padx=5)

tk.Label(frame, text="To:", font=("Arial", 11)).grid(row=0, column=2, padx=5)
dest_lang = ttk.Combobox(frame, values=list(languages.keys()), width=15, state="readonly")
dest_lang.set("Hindi")
dest_lang.grid(row=0, column=3, padx=5)

# Translated Output
tk.Label(root, text="Translated Text:", font=("Arial", 12)).pack(pady=5)
output_text = tk.Text(root, height=5, font=("Arial", 12))
output_text.pack(padx=10, pady=5, fill=tk.X)

# --- Functions ---

def translate_text():
    text = input_text.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Empty Text", "Please enter text to translate.")
        return
    try:
        src = languages[src_lang.get()]
        dest = languages[dest_lang.get()]
        translated = GoogleTranslator(source=src, target=dest).translate(text)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated)
        save_history(text, translated, src_lang.get(), dest_lang.get())
    except Exception as e:
        messagebox.showerror("Translation Error", str(e))

def speak_text():
    text = output_text.get("1.0", tk.END).strip()
    if text:
        tts_engine.say(text)
        tts_engine.runAndWait()

def save_history(orig, translated, src, dest):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    history.append({
        "time": timestamp,
        "source": src,
        "target": dest,
        "input": orig,
        "output": translated
    })

def export_history():
    if not history:
        messagebox.showinfo("No History", "No translation history to export.")
        return
    try:
        with open("translation_history.json", "w", encoding='utf-8') as f:
            json.dump(history, f, indent=4, ensure_ascii=False)
        messagebox.showinfo("Exported", "Translation history saved to translation_history.json")
    except Exception as e:
        messagebox.showerror("Export Error", str(e))

# --- Buttons ---

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="🔁 Translate", font=("Arial", 11), command=translate_text).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="🔊 Speak", font=("Arial", 11), command=speak_text).grid(row=0, column=1, padx=10)
tk.Button(btn_frame, text="💾 Export History", font=("Arial", 11), command=export_history).grid(row=0, column=2, padx=10)

# Start GUI loop
root.mainloop()
