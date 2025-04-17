import os

TODO_FILE = "todo.txt"

def add_task(task):
    with open(TODO_FILE, "a") as file:
        file.write(task + "\n")
    print("Task added!")

def view_tasks():
    if not os.path.exists(TODO_FILE):
        print("No tasks found.")
        return
    with open(TODO_FILE, "r") as file:
        tasks = file.readlines()
    if not tasks:
        print("No tasks found.")
    else:
        print("Your To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task.strip()}")

def delete_task(index):
    if not os.path.exists(TODO_FILE):
        print("No tasks to delete.")
        return
    with open(TODO_FILE, "r") as file:
        tasks = file.readlines()
    if 0 < index <= len(tasks):
        removed = tasks.pop(index - 1)
        with open(TODO_FILE, "w") as file:
            file.writelines(tasks)
        print(f"Deleted: {removed.strip()}")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_tasks()
            try:
                task_num = int(input("Enter task number to delete: "))
                delete_task(task_num)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
  
