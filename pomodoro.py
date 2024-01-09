import tkinter as tk
from tkinter import messagebox
import time

class PomodoroTimer:
    def __init__(self, master):
        self.master = master
        master.title("Pomodoro Timer")

        # Set the time for work period (25 minutes) and break period (5 minutes)
        self.work_time = 25 * 60
        self.short_break_time = 5 * 60
        self.current_time = self.work_time
        self.running = False

        self.timer_label = tk.Label(master, text=self.format_time(self.current_time), font=("Helvetica", 48))
        self.timer_label.pack()

        self.start_button = tk.Button(master, text="Start Work", command=self.start_work)
        self.start_button.pack()

        self.start_break_button = tk.Button(master, text="Start Break", command=self.start_break)
        self.start_break_button.pack()

        self.reset_button = tk.Button(master, text="Reset", command=self.reset)
        self.reset_button.pack()

        self.update_timer()

    def format_time(self, seconds):
        mins, secs = divmod(seconds, 60)
        return f"{mins:02}:{secs:02}"

    def update_timer(self):
        if self.running:
            self.current_time -= 1
            if self.current_time <= 0:
                self.running = False
                if self.current_time == 0:
                    messagebox.showinfo("Time's up!", "Your time is up!")
                self.current_time = self.work_time

        self.timer_label.config(text=self.format_time(self.current_time))
        self.master.after(1000, self.update_timer)

    def start_work(self):
        self.running = True
        self.current_time = self.work_time

    def start_break(self):
        self.running = True
        self.current_time = self.short_break_time

    def reset(self):
        self.running = False
        self.current_time = self.work_time
        self.timer_label.config(text=self.format_time(self.current_time))

root = tk.Tk()
my_timer = PomodoroTimer(root)
root.mainloop()

