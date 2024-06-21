import json
import os

TODO_FILE = 'todo_list.json'

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TODO_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks, title, description):
    task = {
        'id': len(tasks) + 1,
        'title': title,
        'description': description,
        'status': 'Pending'
    }
    tasks.append(task)
    save_tasks(tasks)

def list_tasks(tasks):
    for task in tasks:
        print(f"{task['id']}. {task['title']} - {task['description']} [{task['status']}]")

def update_task(tasks, task_id, title=None, description=None, status=None):
    for task in tasks:
        if task['id'] == task_id:
            if title:
                task['title'] = title
            if description:
                task['description'] = description
            if status:
                task['status'] = status
            save_tasks(tasks)
            return
    print("Task not found!")

def delete_task(tasks, task_id):
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)
    return tasks

def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            add_task(tasks, title, description)
        elif choice == '2':
            list_tasks(tasks)
        elif choice == '3':
            task_id = int(input("Enter task ID to update: "))
            title = input("Enter new title (leave blank to keep current): ")
            description = input("Enter new description (leave blank to keep current): ")
            status = input("Enter new status (leave blank to keep current): ")
            update_task(tasks, task_id, title, description, status)
        elif choice == '4':
            task_id = int(input("Enter task ID to delete: "))
            tasks = delete_task(tasks, task_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()