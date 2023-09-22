from tkinter import *
import datetime
import time
import pygame
from threading import *

# Initialize pygame mixer
pygame.mixer.init()

# Create Object
win = Tk()

# Set geometry
win.geometry("420x180")
win.maxsize(420, 180)
win.minsize(420, 180)

# Use Threading
def Threading():
    t1 = Thread(target=alarm)
    t1.start()

def alarm():
    # Infinite Loop
    print('Alarm is Set :) ')
    while True:
        # Set Alarm
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"

        # Wait for one second
        time.sleep(1)

        # Get current time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")

        # Check whether set alarm is equal to current time or not
        if current_time == set_alarm_time:
            print("Time to Wake up")
            # Play audio for 8 seconds
            pygame.mixer.music.load("Alarm.mp3")
            pygame.mixer.music.play()
            time.sleep(8)  # Wait for 8 seconds
            pygame.mixer.music.stop()

# Add Labels, Frame, Button, Optionmenus
Label(win, text="DIGITAL ALARM", font=("Helvetica 20 bold"), fg="red").pack(pady=10)
Label(win, text="SET TIME", font=("Helvetica 15 bold")).pack()

frame = Frame(win)
frame.pack()

hour = StringVar(win)
hours = tuple(f"{i:02d}" for i in range(25))
hour.set(hours[0])

hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)

minute = StringVar(win)
minutes = tuple(f"{i:02d}" for i in range(61))
minute.set(minutes[0])

mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)

second = StringVar(win)
seconds = tuple(f"{i:02d}" for i in range(61))
second.set(seconds[0])

secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)

Button(win, text="Set Alarm", font=("Helvetica 15"), command=Threading).pack(pady=20)

# Execute Tkinter
win.mainloop()
