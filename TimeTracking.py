import tkinter as tk
import time

# Variable to keep track of elapsed seconds
elapsed_seconds = 0
# Keep track of the scheduled "after" call
timer_job = None
# Variables to store mouse position
offset_x = 0
offset_y = 0

root = tk.Tk()
root.title("Task Timer")

# keep window above others
root.attributes("-topmost", True)

# small fixed size
root.geometry("400x80")

def on_click(event):
    global offset_x, offset_y
    offset_x = event.x
    offset_y = event.y

def on_drag(event):
    x = root.winfo_pointerx() - offset_x
    y = root.winfo_pointery() - offset_y
    root.geometry(f"+{x}+{y}")

# Bind mouse events to the window
root.bind("<Button-1>", on_click)      # Mouse click
root.bind("<B1-Motion>", on_drag)      # Mouse drag

# Label to hold the time
label = tk.Label(root, text="00:00:00")
label.pack()

# Create a frame to hold buttons horizontally
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

def start_timer():
    global elapsed_seconds, timer_job

    # If the timer is already running, do nothing
    if timer_job is not None:
        return

    def update():
        global elapsed_seconds, timer_job
        elapsed_seconds += 1
        hours = elapsed_seconds // 3600
        minutes = (elapsed_seconds % 3600) // 60
        seconds = elapsed_seconds % 60
        label.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")
        
        # Schedule next update and save the job id
        timer_job = root.after(1000, update)

    # Schedule the first update immediately and save the job id
    timer_job = root.after(1000, update)

# Start button
start_button = tk.Button(button_frame, text="Start", command=start_timer)
start_button.pack(side="left", padx=5)

def stop_timer():
    global timer_job
    if timer_job is not None:
        root.after_cancel(timer_job)
        timer_job = None

# Stop button
stop_button = tk.Button(button_frame, text="Stop", command=stop_timer)
stop_button.pack(side="left", padx=5)

def reset_timer():
    global elapsed_seconds, timer_job
    # Stop the timer if it’s running
    if timer_job is not None:
        root.after_cancel(timer_job)
        timer_job = None
    
    # Reset the elapsed time and update label
    elapsed_seconds = 0
    label.config(text="00:00:00")

# Reset button
reset_button = tk.Button(button_frame, text="Reset", command=reset_timer)
reset_button.pack(side="left", padx=5)


root.mainloop()