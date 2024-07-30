import tkinter as tk
from tkinter import messagebox
def Mini_Calculator():
    try:
        Value_1 = float(entry_Value_1.get())
        Value_2 = float(entry_Value_2.get())
        operation = operation_var.get()
        if operation == '+':
            result = Value_1 + Value_2
        elif operation == '-':
            result = Value_1 - Value_2
        elif operation == '*':
            result = Value_1 * Value_2
        elif operation == '/':
            if Value_2 == 0:
                raise ValueError("Division by zero")
            result = Value_1 / Value_2
        else:
            raise ValueError("Invalid operation")
        result_label.config(text=f"Result: {result:.2f}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x400")
root.resizable(False, False)
tk.Label(root, text="Enter First Number:").pack(pady=10)
entry_Value_1 = tk.Entry(root)
entry_Value_1.pack()
tk.Label(root, text="Enter Second Number:").pack(pady=10)
entry_Value_2 = tk.Entry(root)
entry_Value_2.pack()
tk.Label(root, text="Choose operation:").pack(pady=10)
operation_var = tk.StringVar(value='+')
operations = ['+', '-', '*', '/']
for op in operations:
    tk.Radiobutton(root, text=op, variable=operation_var, value=op).pack()
Mini_Calculator_button = tk.Button(root, text="Mini_Calculator", command=Mini_Calculator)
Mini_Calculator_button.pack(pady=20)
result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=10)
root.mainloop()