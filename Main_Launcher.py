import tkinter as tk
import subprocess
import sys
import os

folder_path = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(folder_path, "Icons", "PP.ico")

root = tk.Tk()
root.title("Launcher")
root.geometry("400x150")
root.iconbitmap(icon_path)

# Function for opening the Productivity Launcher
def openProductivity():
    productivity_path = os.path.join(folder_path, "Productivity_Launcher.py")
    subprocess.Popen([sys.executable, productivity_path])

# Function for opening the Health Launcher
def openHealth():
    # TODO: To be completed
    # health_path = os.path.join(folder_path, "Health_Launcher.py")
    # subprocess.Popen([sys.executable, health_path])
    # TODO: Remove when function is complete
    return

# Productivity Button
productivity_button = tk.Button(root, text="Productivity", width=10, command=openProductivity)
productivity_button.pack(pady=10)

# Health Button
health_button = tk.Button(root, text="Health", width=10, command=openHealth)
health_button.pack(pady=10)

root.mainloop()


