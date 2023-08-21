from tkinter import *
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(END, task)
        entry_task.delete(0, END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    if delete_task:
        index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(index)
    else :
        messagebox.showwarning("Warning", "Please select a task to delete.")

def clear_tasks():
    listbox_tasks.delete(0, END)
    
    
main_scr=Tk()
main_scr.geometry("390x605")
# main_scr.resizable(False,False)
main_scr.title("TO-DO List")
main_scr.config(bg="#c0c0c0")


# Entry
entry_task =Entry(main_scr, width=40)
entry_task.pack(pady=10)

# Task List
listbox_tasks = Listbox(main_scr, height=10, width=40, selectbackground="yellow")
listbox_tasks.pack()

# Scrollbar
scrollbar_tasks = Scrollbar(main_scr)
scrollbar_tasks.pack(side=RIGHT, fill=Y)

# Connect the Listbox to the Scrollbar
listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

# Buttons
btn_add_task = Button(main_scr, text="Add Task", width=20, command=add_task)
btn_add_task.pack(pady=5)

btn_delete_task = Button(main_scr, text="Delete Task", width=20, command=delete_task)
btn_delete_task.pack(pady=5)

btn_clear_tasks = Button(main_scr, text="Clear All Tasks", width=20, command=clear_tasks)
btn_clear_tasks.pack(pady=5)


main_scr.mainloop()