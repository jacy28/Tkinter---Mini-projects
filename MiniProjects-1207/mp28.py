# 48. QR Code Generator and Scanner
# •	Input text/link
# •	Generate QR with qrcode
# •	Save as PNG
# •	Scan QR using webcam + opencv
# •	Show decoded data

import tkinter as tk
from tkinter import filedialog, messagebox
import qrcode
from PIL import Image, ImageTk
import cv2
from pyzbar.pyzbar import decode
import threading

def generate_qr():
    data = input_var.get()
    if not data:
        messagebox.showerror("Error", "Please enter text or a link.")
        return

    qr = qrcode.make(data)
    qr.save("qr_output.png")
    img = Image.open("qr_output.png").resize((200, 200))
    qr_img = ImageTk.PhotoImage(img)
    qr_label.config(image=qr_img)
    qr_label.image = qr_img
    messagebox.showinfo("Saved", "QR Code saved as 'qr_output.png'")

def scan_qr():
    def _scan():
        cap = cv2.VideoCapture(0)
        found = False
        while not found:
            ret, frame = cap.read()
            for code in decode(frame):
                qr_data = code.data.decode('utf-8')
                decoded_var.set(qr_data)
                found = True
                break
            cv2.imshow("Scan QR - Press Q to quit", frame)
            if cv2.waitKey(1) & 0xFF == ord('q') or found:
                break
        cap.release()
        cv2.destroyAllWindows()

    threading.Thread(target=_scan).start()

# GUI Setup
root = tk.Tk()
root.title("QR Code Generator & Scanner")
root.geometry("500x400")

input_var = tk.StringVar()
decoded_var = tk.StringVar()

tk.Label(root, text="Enter text or URL:").pack(pady=5)
tk.Entry(root, textvariable=input_var, width=40).pack()

tk.Button(root, text="Generate QR Code", command=generate_qr).pack(pady=10)

qr_label = tk.Label(root)
qr_label.pack(pady=10)

tk.Button(root, text="Scan QR from Webcam", command=scan_qr).pack(pady=10)

tk.Label(root, text="Scanned Result:").pack()
tk.Entry(root, textvariable=decoded_var, width=40).pack()

root.mainloop()
