import tkinter as tk
import time
from datetime import datetime, timedelta

# Create a GUI window
root = tk.Tk()
root.title("Pomodoro Timer")

# Set the window size and position
window_width = 300
window_height = 150
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width / 2) - (window_width / 2))
y_cordinate = int((screen_height / 2) - (window_height / 2))
root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

# Current Time Label
current_time_label = tk.Label(text="", font=("Helvetica", 20))
current_time_label.pack()

# Timer Label
timer_label = tk.Label(text="", font=("Helvetica", 30))
timer_label.pack()

# Start Button
start_button = tk.Button(text="Start", font=("Helvetica", 10))
start_button.pack(side="left")

# Stop Button
stop_button = tk.Button(text="Stop", font=("Helvetica", 10))
stop_button.pack(side="right")

# Variable to track if the timer is running
timer_running = False

# Start Button Functionality
def start_timer():
    global timer_running
    current_time_label.config(text=time.strftime("%H:%M:%S"))
    timer_label.config(text="25:00")
    start_button.config(state="disabled")
    stop_button.config(state="normal")
    timer_running = True
    countdown(25 * 60) # Convert minutes to seconds

# Stop Button Functionality
def stop_timer():
    global timer_running
    timer_running = False
    timer_label.config(text="")
    start_button.config(state="normal")
    stop_button.config(state="disabled")

# Timer Functionality
def countdown(seconds):
    global timer_running
    if seconds <= 0 or not timer_running:
        timer_label.config(text="Time's Up!" if seconds <= 0 else "")
        start_button.config(state="normal")
        stop_button.config(state="disabled")
        return
    
    
    minutes, sec = divmod(seconds, 60)
    timer_label.config(text='{:02d}:{:02d}'.format(minutes, sec))
    root.after(1000, countdown, seconds -1)
   

# This piece of code is used to connect the start and stop button to make it easier
start_button.config(command=lambda: (start_timer(), countdown(25 * 60)))
stop_button.config(command=stop_timer)

root.mainloop()
