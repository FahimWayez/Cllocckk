# Install pip in your computer and then run the following command in the command prompt
# pip install tk

import tkinter as tk
import time
import math

def updateDigitalClock():
    currentTime = time.strftime("%I:%M:%S %p")
    digitalClock.config(text=currentTime)
    digitalClock.after(1000, updateDigitalClock)

def updateAnalogClock():
    currentTime = time.localtime()
    seconds = currentTime.tm_sec
    minutes = currentTime.tm_min
    hours = currentTime.tm_hour % 12

    secAngle = (seconds / 60) * 360
    minAngle = ((minutes + seconds / 60) / 60) * 360
    hourAngle = ((hours + minutes / 60) / 12) * 360

    analogClockCanvas.delete("hands")
    analogClockCanvas.create_line(150, 150, 150 + 50 * math.cos(math.radians(90 - minAngle)), 150 - 50 * math.sin(math.radians(90 - minAngle)), fill="blue", width=2, tags="hands")
    analogClockCanvas.create_line(150, 150, 150 + 40 * math.cos(math.radians(90 - hourAngle)), 150 - 40 * math.sin(math.radians(90 - hourAngle)), fill="green", width=4, tags="hands")
    analogClockCanvas.create_line(150, 150, 150 + 60 * math.cos(math.radians(90 - secAngle)), 150 - 60 * math.sin(math.radians(90 - secAngle)), fill="red", width=1, tags="hands")

    analogClockCanvas.after(1000, updateAnalogClock)

root = tk.Tk()
root.title("Clock")
root.geometry("400x400")
root.config(bg="lightgray")

digitalClock = tk.Label(root, font=("Helvetica", 36), bg="lightgray", fg="blue")
digitalClock.pack(pady=20)

analogClockCanvas = tk.Canvas(root, width=300, height=300, bg="lightgray")
analogClockCanvas.pack()

analogClockCanvas.create_oval(50, 50, 250, 250, width=2, outline="blue")
analogClockCanvas.create_oval(150, 150, 152, 152, fill="red")

for i in range(12):
    angle = math.radians(30 * i)
    x1 = 150 + 80 * math.cos(angle)
    y1 = 150 - 80 * math.sin(angle)
    x2 = 150 + 70 * math.cos(angle)
    y2 = 150 - 70 * math.sin(angle)
    analogClockCanvas.create_line(x1, y1, x2, y2, width=4, fill="blue")

updateDigitalClock()
updateAnalogClock()

root.mainloop()
