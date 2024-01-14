import tkinter as tk
from tkinter import messagebox
from doc_page import HealthHubDoc
from pat_page import HealthHubPat
from create_acc import createaccount
import csv
import server

def account():
    root = tk.Tk()
    acc = createaccount(root)
    root.mainloop()

def Health_hub_doc():
    root = tk.Tk()
    app = HealthHubDoc(root)
    root.mainloop()

def Health_hub_pat():
    root = tk.Tk()
    app = HealthHubPat(root)
    root.mainloop()

def main():
    root = tk.Tk()
    root.title("Sign In")

    app = Application(master=root)
    app.mainloop()

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Doctor(User):
    def __init__(self, username, password):
        super().__init__(username, password)

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.load_users_and_doctors()

    def load_users_and_doctors(self):
        self.users = {}
        self.doctors = {}

        with open('users.csv', 'r') as file:
            reader = csv.reader(file)
            try:
                next(reader)
            except StopIteration:
                pass

            for row in reader:
                username, password, user_type = row
                user = User(username, password)
                self.users[username] = user

                if user_type == 'Doctor':
                    doctor = Doctor(username, password)
                    self.doctors[username] = doctor

    def create_widgets(self):
        self.username_label = tk.Label(self)
        self.username_label["text"] = "Username:"
        self.username_label.pack(side="top")

        self.username_entry = tk.Entry(self)
        self.username_entry["width"] = 30
        self.username_entry.pack(side="top")

        self.password_label = tk.Label(self)
        self.password_label["text"] = "Password:"
        self.password_label.pack(side="top")

        self.password_entry = tk.Entry(self)
        self.password_entry["width"] = 30
        self.password_entry.pack(side="top")
        self.password_entry.config(show="*")

        self.sign_in_button_pat = tk.Button(self)
        self.sign_in_button_pat["text"] = "Patient Login"
        self.sign_in_button_pat["command"] = self.sign_in_pat
        self.sign_in_button_pat.pack(side="top")

        self.sign_in_button_doc = tk.Button(self)
        self.sign_in_button_doc["text"] = "Doctor Login"
        self.sign_in_button_doc["command"] = self.sign_in_doc
        self.sign_in_button_doc.pack(side="top")

        self.account_button = tk.Button(self)
        self.account_button["text"] = "Create account"
        self.account_button["command"] = self.create
        self.account_button.pack(side="top")

        self.exit_button = tk.Button(self)
        self.exit_button["text"] = "Exit"
        self.exit_button["command"] = self.master.destroy
        self.exit_button.pack(side="top")

    def sign_in_doc(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        doctor = self.doctors.get(username)
        if doctor and doctor.password == password:
            messagebox.showinfo("Sign In Successful", "Welcome Doctor " + username)
            self.master.destroy()
            Health_hub_doc()

        else:
            messagebox.showerror("Sign In Failed", "Incorrect username or password for Doctor.")

    def sign_in_pat(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        user = self.users.get(username)
        if user and user.password == password:
            messagebox.showinfo("Sign In Successful", f"Welcome, {user.username}!")
            self.master.destroy()
            self.open_patient_dashboard(username)
            Health_hub_pat()
        else:
            messagebox.showerror("Sign In Failed", "Incorrect username or password for Patient.")

    def open_patient_dashboard(self, username):
        patient_root = tk.Tk()
        HealthHubPat(patient_root, username)
        patient_root.mainloop()

    def create(self):
        account()

if __name__ == "__main__":
    main()
