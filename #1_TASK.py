#CODE_SOFT_PYTHON
#TASK_1_ 
#TO_DO_LIST
import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to remove.")

# Create the main window
app = tk.Tk()
app.title("To-Do List")

# Entry widget for adding tasks
entry = tk.Entry(app, width=40)
entry.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

# Button to add tasks
add_button = tk.Button(app, text="Add Task", command=add_task)
add_button.grid(row=0, column=2, padx=5, pady=10)

# Listbox to display tasks
listbox = tk.Listbox(app, selectmode=tk.SINGLE, width=40, height=10)
listbox.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

# Button to remove selected task
remove_button = tk.Button(app, text="Remove Task", command=remove_task)
remove_button.grid(row=1, column=2, padx=5, pady=10)

# Run the application
app.mainloop()
