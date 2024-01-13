import tkinter as tk
from medical_record import medical_info
from client import ChatClient
from viweappointments import appoint
def chat():
    root = tk.Tk()
    client = ChatClient(root)
    root.mainloop()

class HealthHubDoc:
    def __init__(self, master):
        self.master = master
        self.master.title("HealthHub")
        self.master.geometry("1000x1500")
        self.master.config(bg="blue")

        self.welcome_label = tk.Label(self.master, text="Welcome to Health_Hub", bg="white", fg="black", font=("Arial", 60))
        self.welcome_label.pack()


        self.medical_record_button = tk.Button(self.master, text="Medical Record", command=self.medical_record, bg="blue", fg="blue", height=15, width=15)
        self.medical_record_button.pack()

        self.chat_button = tk.Button(self.master, text="Chat", command=self.chat, bg="blue", fg="blue", height=15, width=15)
        self.chat_button.pack()

        self.schedule_appointment_button = tk.Button(self.master, text="Schedule Appointment", command=self.schedule_appointment, bg="blue", fg="blue", height=15, width=15)
        self.schedule_appointment_button.pack()

        self.exit_button = tk.Button(self.master, text="Exit", command=self.master.quit, bg="blue", fg="blue", height=15, width=15)
        self.exit_button.pack()

    def medical_record(self):

        medical_info()
    def chat(self):
        chat()

    def schedule_appointment(self):
        appoint()

