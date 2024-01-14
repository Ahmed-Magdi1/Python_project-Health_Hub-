import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

class ChatClient:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat Application")


        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(('127.0.0.1', 12345))


        self.chat_area = scrolledtext.ScrolledText(root)
        self.chat_area.pack(padx=20, pady=5)
        self.chat_area.config(state=tk.DISABLED)

        self.msg_entry = tk.Entry(root)
        self.msg_entry.pack(padx=20, pady=5)

        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.pack(padx=20, pady=5)

        self.receive_thread = threading.Thread(target=self.receive_messages)
        self.receive_thread.start()

    def send_message(self):
        message = self.msg_entry.get()
        self.sock.send(message.encode('utf-8'))
        self.msg_entry.delete(0, tk.END)

    def receive_messages(self):
        while True:
            try:
                message = self.sock.recv(1024).decode('utf-8')
                self.chat_area.config(state=tk.NORMAL)
                self.chat_area.insert(tk.END, message + '\n')
                self.chat_area.yview(tk.END)
                self.chat_area.config(state=tk.DISABLED)
            except ConnectionAbortedError:
                break
            except:
                print("An error occurred!")
                self.sock.close()
                break


