# 28. Simple Music Composer using MIDI
# •	Piano key GUI (Canvas/buttons)
# •	Click to play notes, record sequence
# •	Save/load MIDI files
# •	Show note timeline
# •	Volume control

import tkinter as tk
from tkinter import messagebox, filedialog
from mido import Message, MidiFile, MidiTrack

# MIDI note numbers for C4 to B4
NOTE_NAMES = [
    ('C', 60), ('C#', 61), ('D', 62), ('D#', 63), ('E', 64),
    ('F', 65), ('F#', 66), ('G', 67), ('G#', 68), ('A', 69), ('A#', 70), ('B', 71)
]

class MidiComposer:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple MIDI Composer")

        self.track = []
        self.recording = False

        self.build_ui()

    def build_ui(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        # Piano keys
        for name, note in NOTE_NAMES:
            color = 'white' if '#' not in name else 'black'
            fg = 'black' if color == 'white' else 'white'
            btn = tk.Button(frame, text=name, bg=color, fg=fg, width=5, command=lambda n=note: self.play_note(n))
            btn.pack(side='left', padx=1)

        # Record/save controls
        control = tk.Frame(self.root)
        control.pack(pady=10)

        tk.Button(control, text="Start Recording", command=self.start_record).pack(side='left', padx=5)
        tk.Button(control, text="Stop Recording", command=self.stop_record).pack(side='left', padx=5)
        tk.Button(control, text="Save MIDI", command=self.save_midi).pack(side='left', padx=5)

        self.listbox = tk.Listbox(self.root, width=40)
        self.listbox.pack(pady=10)

    def play_note(self, note):
        if self.recording:
            self.track.append((note, 480))  # fixed duration for simplicity
            self.listbox.insert('end', f"Note {note} recorded")
        else:
            messagebox.showinfo("Note Played", f"Played note: {note}")

    def start_record(self):
        self.track.clear()
        self.listbox.delete(0, 'end')
        self.recording = True
        messagebox.showinfo("Recording", "Recording started.")

    def stop_record(self):
        self.recording = False
        messagebox.showinfo("Recording", "Recording stopped.")

    def save_midi(self):
        if not self.track:
            messagebox.showwarning("Empty", "No notes recorded.")
            return

        mid = MidiFile()
        track = MidiTrack()
        mid.tracks.append(track)

        track.append(Message('program_change', program=0, time=0))
        for note, duration in self.track:
            track.append(Message('note_on', note=note, velocity=64, time=0))
            track.append(Message('note_off', note=note, velocity=64, time=duration))

        file_path = filedialog.asksaveasfilename(defaultextension=".mid", filetypes=[("MIDI files", "*.mid")])
        if file_path:
            mid.save(file_path)
            messagebox.showinfo("Saved", f"MIDI saved to {file_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MidiComposer(root)
    root.mainloop()
