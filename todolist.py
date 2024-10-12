# Simple To-Do List Application

todo_list = []

def add_task():
    task = input("Enter a task: ")
    todo_list.append(task)
    print(f"Task '{task}' added.")

def view_tasks():
    if not todo_list:
        print("No tasks in the to-do list.")
    else:
        print("To-Do List:")
        for idx, task in enumerate(todo_list, start=1):
            print(f"{idx}. {task}")

def delete_task():
    view_tasks()
    try:
        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(todo_list):
            removed_task = todo_list.pop(task_number - 1)
            print(f"Task '{removed_task}' removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def show_menu():
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            print("Exiting To-Do List Application.")
            break
        else:
            print("Invalid choice, please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
