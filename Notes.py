import tkinter as tk
from tkinter import filedialog, messagebox
import os

### Global Variables ###

# This variable will store the file location for the currently opened note.
current_file = None

root = tk.Tk()
root.title("Quick Notes")

# Small fixed size
root.geometry("400x200")
# Make the window always stay on top
root.attributes("-topmost", True)

# Text widget for writing notes
text_area = tk.Text(root, wrap="word")
text_area.pack(expand=True, fill="both")

# Function for saving the note.
def save_file():
    global current_file

    if current_file is None:
        save_as_file()
    else:
        try:
            # Get the text in the Notes window starting at the beginning and ending at the end - 1 character.
            content = text_area.get("1.0", "end-1c")
            # Use utf-8 encoding for compatibility
            with open(current_file, 'w', encoding='utf-8') as f:
                      f.write(content)
                      messagebox.showinfo("Saved", f"File saved to:\n{current_file}")
        except Exception as e:
            messagebox.showerror("Error", f"Could not save file:\n{str(e)}")

# Method to save a file by browsing for a location to save it.
def save_as_file():
     global current_file

     file_path = filedialog.asksaveasfilename(
          defaultextension=".txt",
          filetypes=[
               ("Text files", "*.txt"),
               ("All files", "*.*")
          ]
     )

     if file_path:
          current_file = file_path
          root.title(f"Quick Notes - {os.path.basename(current_file)}")
          save_file()
          
# Function to load txt files into a note window
def open_file():
     global current_file

     file_path = filedialog.askopenfilename(
          defaultextension=".txt",
          filetypes=[
               ("Text files", "*.txt"),
               ("All files", "*.*")
          ]
     )

     if file_path:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Clear the current text
            text_area.delete("1.0", "end")
            
            # Insert the loaded content
            text_area.insert("1.0", content)

            # Update current_file
            current_file = file_path

            # Update window title
            root.title(f"Quick Notes - {os.path.basename(current_file)}")

        except Exception as e:
             messagebox.showerror("Error", f"Could not open file:\n{str(e)}")
        

# Create a context menu
context_menu = tk.Menu(root, tearoff=0)
context_menu.add_command(label="Open...", command=open_file)
context_menu.add_separator()
context_menu.add_command(label="Cut", command=lambda: text_area.event_generate("<<Cut>>"))
context_menu.add_command(label="Copy", command=lambda: text_area.event_generate("<<Copy>>"))
context_menu.add_command(label="Paste", command=lambda: text_area.event_generate("<<Paste>>"))
context_menu.add_separator()
context_menu.add_command(label="Save", command=save_file)
context_menu.add_command(label="Save As...", command = save_as_file)

# Function to show the menu on right-click
def show_context_menu(event):
    context_menu.tk_popup(event.x_root, event.y_root)

# Bind right-click to show the menu
text_area.bind("<Button-3>", show_context_menu)

root.mainloop()