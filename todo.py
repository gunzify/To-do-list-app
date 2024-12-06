# todo.py

def display_tasks(tasks):
    """Display the list of tasks."""
    print("\nTo-Do List:")
    if not tasks:
        print("No tasks yet!")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "[x]" if task['completed'] else "[ ]"
            print(f"{i}. {status} {task['title']}")
    print()

def add_task(tasks):
    """Add a new task to the list."""
    title = input("Enter task title: ").strip()
    tasks.append({"title": title, "completed": False})
    print(f"Task '{title}' added!\n")

def mark_task_completed(tasks):
    """Mark a task as completed."""
    try:
        task_number = int(input("Enter task number to mark as completed: "))
        tasks[task_number - 1]['completed'] = True
        print("Task marked as completed!\n")
    except (IndexError, ValueError):
        print("Invalid task number!\n")

def delete_task(tasks):
    """Delete a task from the list."""
    try:
        task_number = int(input("Enter task number to delete: "))
        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task['title']}' deleted!\n")
    except (IndexError, ValueError):
        print("Invalid task number!\n")

def main():
    tasks = []
    while True:
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as completed")
        print("4. Delete task")
        print("5. Exit")
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")

if __name__ == "__main__":
    main()
