import json
import os

# File to store tasks
TASK_FILE = "tasks.json"

# Load tasks from the file
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    return []

# Save tasks to the file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    task = {
        "title": title,
        "description": description,
        "completed": False
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{title}' added.")

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for index, task in enumerate(tasks, start=1):
            status = "✓" if task["completed"] else "✗"
            print(f"{index}. {task['title']} - {task['description']} [{status}]")

# Update an existing task
def update_task(tasks):
    view_tasks(tasks)
    if tasks:
        task_number = int(input("Enter the task number to update: "))
        if 1 <= task_number <= len(tasks):
            task = tasks[task_number - 1]
            task["title"] = input(f"Enter new title for '{task['title']}' (or press Enter to keep it the same): ") or task["title"]
            task["description"] = input(f"Enter new description for '{task['description']}' (or press Enter to keep it the same): ") or task["description"]
            save_tasks(tasks)
            print(f"Task {task_number} updated.")
        else:
            print("Invalid task number.")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(tasks):
            deleted_task = tasks.pop(task_number - 1)
            save_tasks(tasks)
            print(f"Task '{deleted_task['title']}' deleted.")
        else:
            print("Invalid task number.")

# Mark a task as completed
def complete_task(tasks):
    view_tasks(tasks)
    if tasks:
        task_number = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            save_tasks(tasks)
            print(f"Task {task_number} marked as completed.")
        else:
            print("Invalid task number.")

# Main menu
def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List")
        print("1. View tasks")
        print("2. Add task")
        print("3. Update task")
        print("4. Delete task")
        print("5. Complete task")
        print("6. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            complete_task(tasks)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
