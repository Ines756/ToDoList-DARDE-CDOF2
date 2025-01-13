import os

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task, priority):
        self.tasks.append({"task": task, "completed": False, "priority": priority})
        print(f"Task '{task}' with priority '{priority}' added!")

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

    def show_tasks(self, hide_completed=False):
        filtered_tasks = [
            (index, task) for index, task in enumerate(self.tasks, 1)
            if not (hide_completed and task["completed"])
        ] # have a list with tasks that are not completed only
        if not filtered_tasks: # no tasks to be marked done
            print("No tasks to display.")
            return
        for index, task in filtered_tasks:
            status = "Done" if task["completed"] else "ToDo"
            priority_color = self.get_priority_color(task["priority"])
            print(f"{index}. {task['task']} [{status}] {priority_color}(Priority: {self.get_priority_text(priority_color)})\033[0m")

    def get_priority_text(self, priority):
        if priority == "Magenta":
            return "High"  
        elif priority == "Green":
            return "Medium" 
        elif priority == "Blue1":
            return "Low" 
        return "Unknown"

    def get_priority_color(self, priority):
        if priority == "High":
            return "\033[95m" 
        elif priority == "Medium":
            return "\033[93m" 
        elif priority == "Low":
            return "\033[94m" 
        return "\033[0m" 
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
            print("Choose a priority for the task:")
            print("1. Magenta (High)")
            print("2. Green (Medium)")
            print("3. Blue (Low)")
            priority_choice = input("Enter priority (1/2/3): ")
            if priority_choice == "1":
                priority = "High"
            elif priority_choice == "2":
                priority = "Medium"
            elif priority_choice == "3":
                priority = "Low"
            else:
                print("Invalid priority choice, defaulting to Green.")
                priority = "Green"
            todo_list.add_task(task, priority)
        elif choice == "2":
            todo_list.show_tasks()
            try:
                task_number = int(input("Enter the task number to remove: "))
                todo_list.remove_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "3":
            print("Tasks available to complete:")
            todo_list.show_tasks(hide_completed=True)  # Masquer les tâches terminées
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
