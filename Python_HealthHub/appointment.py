import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
import csv

class Appointment(tk.Toplevel):
    def __init__(self,username):
        super().__init__()
        self.username = username
        self.geometry("500x500")
        self.title("Appointment Scheduler")
        self.create_widgets()

    def create_widgets(self):
        self.my_label = tk.Label(self, text="Book an appointment")
        self.my_label.pack(pady=5)

        self.appointment_date = tk.StringVar()
        self.appointment_time = tk.StringVar()


        print("Creating date and time comboboxes...")

        dates = self.get_available_dates()
        print("Available dates:", dates)
        self.appointment_date_entry = ttk.Combobox(self, textvariable=self.appointment_date, values=dates)
        self.appointment_date_entry.pack(pady=10)

        times = self.get_available_times()
        print("Available times:", times)
        self.appointment_time_entry = ttk.Combobox(self, textvariable=self.appointment_time, values=times)
        self.appointment_time_entry.pack(pady=10)

        self.submit_button = ttk.Button(self, text="Submit", command=self.submit_appointment)
        self.submit_button.pack(pady=10)

        self.back_button = ttk.Button(self, text="Back to Main Page", command=self.close_scheduler)
        self.back_button.pack(pady=10)

    def submit_appointment(self):
        current_user = self.get_current_user()

        appointment_date = self.appointment_date.get()
        appointment_time = self.appointment_time.get()
        if self.validate_appointment_date(appointment_date) and self.validate_appointment_time(appointment_time):
            messagebox.showinfo("Success", f"Appointment booked successfully for {appointment_date} at {appointment_time}")

            self.save_appointment_to_csv(current_user, appointment_date, appointment_time)
        else:
            messagebox.showerror("Error", "Invalid appointment date or time. Please try again.")

    def save_appointment_to_csv(self, user, date, time):

        csv_file_path = 'appointments.csv'


        appointment_data = [user, date, time]
        try:
            with open(csv_file_path, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(appointment_data)
        except IOError as e:
            messagebox.showerror("Error", f"Failed to save appointment: {e}")

    def validate_appointment_date(self, date):
        try:
            datetime.strptime(date, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    def validate_appointment_time(self, time):
        try:
            datetime.strptime(time, "%H:%M")
            return True
        except ValueError:
            return False

    def get_available_dates(self):
        current_date = datetime.now().date()
        available_dates = [(current_date + timedelta(days=x)).strftime("%Y-%m-%d") for x in range(5)]
        return available_dates

    def get_available_times(self):
        current_time = datetime.now().time()
        available_times = [(datetime.now() + timedelta(hours=x)).strftime("%H:%M") for x in range(8, 18)]
        return available_times

    def close_scheduler(self):
        self.destroy()
        self.deiconify()

    def get_current_user(self):

        return self.username