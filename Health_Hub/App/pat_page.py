import tkinter as tk
from appointment import Appointment
from client import ChatClient
from patient_medcialreport import patient_info



def chat():
    root = tk.Tk()
    client = ChatClient(root)
    root.mainloop()
def appointment(username):
    app = Appointment(username)
    app.mainloop()
class HealthHubPat:
    def __init__(self, master, username):
        self.master = master
        self.username = username
        self.master.title("HealthHub")
        self.master.geometry("1000x1500")
        self.master.config(bg="green")

        self.welcome_label = tk.Label(self.master, text=f"Welcome {self.username}", bg="white", fg="black",
                                      font=("Arial", 60))
        self.welcome_label.pack()


        self.medical_record_button = tk.Button(self.master, text="Medical Record", command=self.medical_record, bg="red", fg="blue", height=15, width=15)
        self.medical_record_button.pack()

        self.chat_button = tk.Button(self.master, text="Chat", command=self.chat, bg="red", fg="blue", height=15, width=15)
        self.chat_button.pack()

        self.schedule_appointment_button = tk.Button(self.master, text="Schedule Appointment", command=self.schedule_appointment, bg="red", fg="blue", height=15, width=15)
        self.schedule_appointment_button.pack()

        self.exit_button = tk.Button(self.master, text="Exit", command=self.master.quit, bg="green", fg="blue", height=15, width=15)
        self.exit_button.pack()

    def medical_record(self):
        patient_info(self.username)
    def chat(self):
        chat()

    def schedule_appointment(self):
        appointment(self.username)



