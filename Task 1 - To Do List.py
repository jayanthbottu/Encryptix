import tkinter as tk
from tkinter import messagebox, simpledialog

class TO_DO_APPLICATION:
    def __init__(self, master):
        self.master = master
        self.master.title("TO-DO LIST")
        self.master.geometry("400x400")

        self.task_list_data = []

        self.task_list = tk.Listbox(self.master, width=50)
        self.task_list.pack(pady=10)

        self.add_button = tk.Button(self.master, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.update_button = tk.Button(self.master, text="Update Task", command=self.update_task)
        self.update_button.pack(pady=5)

        self.delete_button = tk.Button(self.master, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.mark_done_button = tk.Button(self.master, text="Mark as Done", command=self.mark_done)
        self.mark_done_button.pack(pady=5)

    def add_task(self):
        task = simpledialog.askstring("Add Task", "Enter a new task:")
        if task and task.strip():
            self.task_list_data.append(task)
            self.update_list()

    def update_task(self):
        try:
            index = self.task_list.curselection()[0]
            task = simpledialog.askstring("Update Task", "Enter the updated task:", initialvalue=self.task_list_data[index])
            if task and task.strip():
                self.task_list_data[index] = task
                self.update_list()
        except IndexError:
            messagebox.showerror("Error", "Please select a task to update.")

    def delete_task(self):
        try:
            index = self.task_list.curselection()[0]
            del self.task_list_data[index]
            self.update_list()
        except IndexError:
            messagebox.showerror("Error", "Please select a task to delete.")

    def mark_done(self):
        try:
            index = self.task_list.curselection()[0]
            self.task_list_data[index] = f"[TASK DONE] {self.task_list_data[index]}"
            self.update_list()
        except IndexError:
            messagebox.showerror("Error", "Please select a task to mark as done.")

    def update_list(self):
        self.task_list.delete(0, tk.END)
        for task in self.task_list_data:
            self.task_list.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TO_DO_APPLICATION(root)
    root.mainloop()