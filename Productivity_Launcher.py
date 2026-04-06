import tkinter as tk
import subprocess
import sys
import os
import threading
import pystray
from PIL import Image

# Folder where the launcher script is located
folder_path = os.path.dirname(os.path.abspath(__file__))
# Path to the main icon.
icon_path = os.path.join(folder_path, "Icons", "PP.ico")

root = tk.Tk()
root.title("Launcher")
root.geometry("400x150")
root.iconbitmap(icon_path)

def quit_window(icon, item=None):
    icon.stop()
    root.quit()

def show_window(icon, item=None):
    icon.stop()
    root.after(0, lambda: (root.deiconify, root.state('normal')))

def hide_to_tray():
    root.withdraw()

    img = Image.open(icon_path)

    menu = (
        pystray.MenuItem('Show Launcher', show_window),
        pystray.MenuItem('Quit Launcher', quit_window)
    )

    icon = pystray.Icon("Productivity Launcher", img, "Productivity Launcher", menu)

    threading.Thread(target=icon.run, daemon=True).start()

def on_minimize(event):
    # Only hide if the window is actually being minimized AND the event is for the main window
    if event.widget == root and root.state() == 'iconic':
        hide_to_tray()

root.bind("<Unmap>", on_minimize)

def open_notes():
    notes_path = os.path.join(folder_path, "notes.py")
    subprocess.Popen([sys.executable, notes_path])

def open_timer():
    timer_path = os.path.join(folder_path, "TimeTracking.py")
    subprocess.Popen([sys.executable, timer_path])

# Notes button
notes_button = tk.Button(root, text="Notes", width=10, command=open_notes)
notes_button.pack(pady=10)

# Timer button
timer_button = tk.Button(root, text="Timer", width=10, command=open_timer)
timer_button.pack()

root.mainloop()