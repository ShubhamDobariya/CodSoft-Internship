import tkinter as tk 
from tkinter import messagebox

def sum(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def calculator():
    try:
        n1 = float(entern1.get())
        n2 = float(entern2.get())
        op = opvar.get()

        if op == "Sum":
            result = sum(n1, n2)
        elif op == "Subtract":
            result = subtract(n1, n2)
        elif op == "Multiply":
            result = multiply(n1, n2)
        elif op == "Divide":
            result = divide(n1, n2)

        label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Entered input is wrong!!", "Please Enter valid numbers.")
    
base = tk.Tk()
base.title("Simple Calculator")


tk.Label(base, text="Enter first number:").grid(row=0, column=0)
entern1 = tk.Entry(base)
entern1.grid(row=0, column=1)

tk.Label(base, text="Enter second number:").grid(row=1, column=0)
entern2 = tk.Entry(base)
entern2.grid(row=1, column=1)

tk.Label(base, text="Choose operation:").grid(row=2, column=0)
opvar = tk.StringVar(value="Sum")
operations = ["Sum", "Subtract", "Multiply", "Divide"]
opmenu = tk.OptionMenu(base, opvar, *operations)
opmenu.grid(row=2, column=1)

calculatebutton = tk.Button(base, text="Calculate", command=calculator)
calculatebutton.grid(row=3, column=0, columnspan=2)

label = tk.Label(base, text="Result: ")
label.grid(row=4, column=0, columnspan=2)

base.mainloop()

