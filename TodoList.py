import os

# A simple class to manage the to-do list
class TodoList:
    def __init__(self):
        self.tasks = [] 

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added!")

    def remove_task(self, task_number):
        try:
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task '{removed_task['task']}' removed!")
        except IndexError:
            print("Invalid task number!")

    def complete_task(self, task_number):
        try:
            self.tasks[task_number - 1]["completed"] = True
            print(f"Task '{self.tasks[task_number - 1]['task']}' marked as completed!")
        except IndexError:
            print("Invalid task number!")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks to display.")
            return
        for index, task in enumerate(self.tasks, 1):
            status = "Done" if task["completed"] else "ToDo"
            print(f"{index}. {task['task']} [{status}]")

def main():
    todo_list = TodoList()

    while True:
        os.system('cls' if os.name == 'nt' else 'clear') 
        print("=== To-Do List ===")
        todo_list.show_tasks()

        print("\nChoose an option:")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. Mark a task as completed")
        print("4. Quit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            task = input("Enter the task description: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.show_tasks()
            try:
                task_number = int(input("Enter the task number to remove: "))
                todo_list.remove_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "3":
            todo_list.show_tasks()
            try:
                task_number = int(input("Enter the task number to mark as completed: "))
                todo_list.complete_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
