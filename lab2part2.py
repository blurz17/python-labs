"""
CRUD Operations

Create - Read - Update - Delete

BONUS:
- Mark task as DONE.
"""

tasks_list = []


# Create
def add_task():
    task = input("Enter your task: ")
    tasks_list.append({"task": task, "done": False})
    print("Task added successfully!\n")


def read_task():
    if not tasks_list:
        print('No Tasks Found!')
    print("These are your Tasks: ")
    
    for i, task in enumerate(tasks_list, start=1):
        print(f"{i}- [{task}]")

# Update
def update_task():
    read_task()

    if not tasks_list:
        return

    index = int(input("Enter task number to update: ")) - 1

    if 0 <= index < len(tasks_list):
        new_task = input("Enter the new task: ")
        tasks_list[index]["task"] = new_task
        print("Task updated successfully!\n")
    else:
        print("Invalid task number!\n")


# Delete
def delete_task():
    read_task()

    if not tasks_list:
        return

    index = int(input("Enter task number to delete: ")) - 1
    if 0 <= index < len(tasks_list):
        deleted = tasks_list.pop(index)
        print(f"Deleted: {deleted['task']}\n")
    else:
        print("Invalid task number!\n")

while True:
    print("TO-DO APPLICATION ")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        read_task()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!\n")