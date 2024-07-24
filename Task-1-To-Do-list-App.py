import tkinter as tk

tasks = []

def newtask():
    task = entrytask.get()
    if task:
        tasks.append(task)
        displaytask()
        entrytask.delete(0, tk.END)

def deletetask():
    index = int(entryindex.get()) - 1
    if 0 <= index < len(tasks):
        removedtask = tasks.pop(index)
        displaytask()

def displaytask():
    listoftasks.delete(0, tk.END)
    for index, task in enumerate(tasks, start=1):
        listoftasks.insert(tk.END, f"{index}. {task}")

base = tk.Tk()
base.title("To-Do List")

labelfortask = tk.Label(base, text="Enter New Task:")
labelfortask.pack()
entrytask = tk.Entry(base, width=40)
entrytask.pack()

Addbutton = tk.Button(base, text="Add Task", command=newtask)
Addbutton.pack()

Clearbutton = tk.Button(base, text="Clear", command=lambda: entrytask.delete(0, tk.END))
Clearbutton.pack()

listoftasks = tk.Listbox(base, width=50)
listoftasks.pack()

labelindex = tk.Label(base, text="Enter Index to Delete:")
labelindex.pack()
entryindex = tk.Entry(base, width=40)
entryindex.pack()

Removebutton = tk.Button(base, text="Delete Task", command=deletetask)
Removebutton.pack()

base.mainloop()
