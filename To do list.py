def display_menu():
    print("To-Do List Menu:")
    print("1. View to-do list")
    print("2. Add a new task")
    print("3. Mark a task as complete")
    print("4. Exit")

def view_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("Your to-do list:")
        for idx, task in enumerate(tasks):
            status = "✓" if task["completed"] else "✗"
            print(f"{idx + 1}. {task['description']} [{status}]")
    print()

def add_task(tasks):
    description = input("Enter the task description: ")
    tasks.append({"description": description, "completed": False})
    print(f"Task '{description}' added.\n")

def mark_task_as_complete(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter the task number to mark as complete: ")) - 1
            if 0 <= task_num < len(tasks):
                tasks[task_num]["completed"] = True
                print(f"Task '{tasks[task_num]['description']}' marked as complete.\n")
            else:
                print("Invalid task number.\n")
        except ValueError:
            print("Please enter a valid number.\n")

def main():
    tasks = []

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task_as_complete(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    main()
