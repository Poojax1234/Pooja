import tkinter as tk
from tkinter import messagebox
import datetime
import time
import winsound

class AlarmClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Alarm Clock")
        self.alarms = []

        self.frame = tk.Frame(root)
        self.frame.pack(pady=20)

        self.label = tk.Label(self.frame, text="Set Alarm (HH:MM):")
        self.label.pack()

        self.entry = tk.Entry(self.frame)
        self.entry.pack()

        self.add_button = tk.Button(self.frame, text="Add Alarm", command=self.add_alarm)
        self.add_button.pack()

        self.alarms_label = tk.Label(self.frame, text="Alarms:")
        self.alarms_label.pack()

        self.alarms_listbox = tk.Listbox(self.frame, selectmode=tk.SINGLE)
        self.alarms_listbox.pack()

        self.remove_button = tk.Button(self.frame, text="Remove Alarm", command=self.remove_alarm)
        self.remove_button.pack()

        self.set_button = tk.Button(self.frame, text="Set Alarms", command=self.set_alarms)
        self.set_button.pack()

        self.status_label = tk.Label(self.frame, text="")
        self.status_label.pack()

    def add_alarm(self):
        alarm_time = self.entry.get()
        try:
            alarm_time = datetime.datetime.strptime(alarm_time, '%H:%M')
            self.alarms.append(alarm_time.time())
            self.alarms_listbox.insert(tk.END, alarm_time.strftime('%H:%M'))
            self.entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Invalid time format (HH:MM)")

    def remove_alarm(self):
        selected_index = self.alarms_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.alarms.pop(index)
            self.alarms_listbox.delete(index)

    def set_alarms(self):
        if not self.alarms:
            self.status_label.config(text="No alarms set.")
            return

        while True:
            current_time = datetime.datetime.now().time()
            for alarm_time in self.alarms:
                if current_time >= alarm_time:
                    winsound.Beep(1000, 1000)  # Beep sound when the alarm goes off
                    self.alarms.remove(alarm_time)
                    index = self.alarms.index(alarm_time)
                    self.alarms_listbox.delete(index)
                    self.status_label.config(text=f"Alarm at {alarm_time.strftime('%H:%M')} triggered.")
            time.sleep(1)

if __name__ == "__main__":
    root = tk.Tk()
    alarm_clock = AlarmClock(root)
    root.mainloop()