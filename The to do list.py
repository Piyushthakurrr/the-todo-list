import json
import os

class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

    def __repr__(self):
        return f"{'[X]' if self.completed else '[ ]'} {self.description}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        self.tasks.append(Task(description))

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        for idx, task in enumerate(self.tasks, start=1):
            print(f"{idx}. {task}")

    def update_task(self, index, description):
        if 0 <= index < len(self.tasks):
            self.tasks[index].description = description
        else:
            print("Invalid task index.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
        else:
            print("Invalid task index.")

    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
        else:
            print("Invalid task index.")

    def save_tasks(self, filename="tasks.json"):
        with open(filename, "w") as file:
            json.dump([task.__dict__ for task in self.tasks], file)

    def load_tasks(self, filename="tasks.json"):
        if os.path.exists(filename):
            with open(filename, "r") as file:
                tasks_data = json.load(file)
                self.tasks = [Task(**data) for data in tasks_data]

def main():
    todo_list = ToDoList()
    todo_list.load_tasks()

    while True:
        print("\nTo-Do List:")
        todo_list.view_tasks()
        print("\nOptions:")
        print("1. Add a new task")
        print("2. Update a task")
        print("3. Delete a task")
        print("4. Mark a task as completed")
        print("5. Save and exit")
        print("6. Exit without saving")

        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == '2':
            index = int(input("Enter task number to update: ")) - 1
            description = input("Enter new description: ")
            todo_list.update_task(index, description)
        elif choice == '3':
            index = int(input("Enter task number to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == '4':
            index = int(input("Enter task number to mark as completed: ")) - 1
            todo_list.mark_completed(index)
        elif choice == '5':
            todo_list.save_tasks()
            break
        elif choice == '6':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
