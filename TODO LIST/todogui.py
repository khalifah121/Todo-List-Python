import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def clear_tasks():
    listbox_tasks.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("To-Do List Application")

# Task Entry
entry_task = tk.Entry(root, width=40)
entry_task.pack(pady=10)

# Task List
listbox_tasks = tk.Listbox(root, height=10, width=40, selectbackground="yellow")
listbox_tasks.pack()

# Scrollbar
scrollbar_tasks = tk.Scrollbar(root)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

# Connect the Listbox to the Scrollbar
listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

# Buttons
btn_add_task = tk.Button(root, text="Add Task", width=20, command=add_task)
btn_add_task.pack(pady=5)

btn_delete_task = tk.Button(root, text="Delete Task", width=20, command=delete_task)
btn_delete_task.pack(pady=5)

btn_clear_tasks = tk.Button(root, text="Clear All Tasks", width=20, command=clear_tasks)
btn_clear_tasks.pack(pady=5)

root.mainloop()
