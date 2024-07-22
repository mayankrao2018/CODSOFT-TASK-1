import tkinter as tk
from tkinter import messagebox

class Mayank_app:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("To-Do List")

        self.tasks = []

        self.task_entry = tk.Entry(self.root, width=40)
        self.task_entry.pack()

        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.task_listbox = tk.Listbox(self.root, width=40)
        self.task_listbox.pack()

        self.remove_button = tk.Button(self.root, text="Delete Task", command=self.remove_tasks)
        self.remove_button.pack()

        self.root.mainloop()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Please enter a task !!!")

    def remove_tasks(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.tasks[index]
            self.update_list()

    def update_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    app = Mayank_app()
