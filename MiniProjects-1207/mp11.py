# 31. Email Automation GUI with Gmail OAuth
# •	Compose email with subject/body
# •	Load recipients from file
# •	Send via Gmail API with OAuth
# •	Show success/failure log
# •	Delay and throttle control

import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import time
import csv
import os

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from email.mime.text import MIMEText
import base64

SCOPES = ['https://www.googleapis.com/auth/gmail.send']

class GmailSenderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Email Automation with Gmail OAuth")

        self.recipients = []
        self.delay = 1

        self.build_gui()
        self.creds = None
        self.service = None

    def build_gui(self):
        tk.Label(self.root, text="Subject").pack()
        self.subject_entry = tk.Entry(self.root, width=80)
        self.subject_entry.pack()

        tk.Label(self.root, text="Message Body").pack()
        self.body_text = scrolledtext.ScrolledText(self.root, width=80, height=10)
        self.body_text.pack()

        tk.Button(self.root, text="Load Recipients", command=self.load_recipients).pack(pady=5)
        tk.Button(self.root, text="Authorize Gmail", command=self.login_gmail).pack(pady=5)
        tk.Button(self.root, text="Send Emails", command=self.send_emails).pack(pady=5)

        tk.Label(self.root, text="Delay between emails (seconds):").pack()
        self.delay_entry = tk.Entry(self.root)
        self.delay_entry.insert(0, "1")
        self.delay_entry.pack()

        tk.Label(self.root, text="Log:").pack()
        self.log_text = scrolledtext.ScrolledText(self.root, width=80, height=10, state='disabled')
        self.log_text.pack()

    def log(self, msg):
        self.log_text.config(state='normal')
        self.log_text.insert(tk.END, msg + '\n')
        self.log_text.see(tk.END)
        self.log_text.config(state='disabled')

    def load_recipients(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text/CSV Files", "*.txt *.csv")])
        if file_path:
            self.recipients.clear()
            with open(file_path, newline='') as f:
                reader = csv.reader(f)
                for row in reader:
                    for item in row:
                        item = item.strip()
                        if '@' in item:
                            self.recipients.append(item)
            self.log(f"Loaded {len(self.recipients)} recipient(s).")

    def login_gmail(self):
        try:
            creds = None
            if os.path.exists('token.json'):
                creds = Credentials.from_authorized_user_file('token.json', SCOPES)
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
                    creds = flow.run_local_server(port=0)
                with open('token.json', 'w') as token:
                    token.write(creds.to_json())

            self.creds = creds
            self.service = build('gmail', 'v1', credentials=creds)
            self.log("Gmail authorized successfully.")
        except Exception as e:
            self.log(f"Authorization error: {e}")
            messagebox.showerror("Auth Error", str(e))

    def create_message(self, to, subject, message_text):
        message = MIMEText(message_text)
        message['to'] = to
        message['subject'] = subject
        raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
        return {'raw': raw}

    def send_emails(self):
        if not self.service:
            messagebox.showerror("Error", "Please authorize Gmail first.")
            return
        if not self.recipients:
            messagebox.showerror("Error", "No recipients loaded.")
            return

        subject = self.subject_entry.get()
        body = self.body_text.get("1.0", tk.END).strip()

        try:
            self.delay = float(self.delay_entry.get())
        except:
            self.delay = 1

        self.log("Starting email send...")
        for i, to in enumerate(self.recipients, 1):
            try:
                message = self.create_message(to, subject, body)
                self.service.users().messages().send(userId="me", body=message).execute()
                self.log(f"{i}. Sent to {to}")
            except Exception as e:
                self.log(f"{i}. Failed to send to {to}: {e}")
            time.sleep(self.delay)
        self.log("All emails processed.")

if __name__ == "__main__":
    root = tk.Tk()
    app = GmailSenderApp(root)
    root.mainloop()
