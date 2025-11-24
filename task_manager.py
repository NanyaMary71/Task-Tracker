
import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []

    with open(TASKS_FILE, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(description):
    tasks = load_tasks()
    new_id = 1 if len(tasks) == 0 else tasks[-1]["id"] + 1
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    task = {
        "id": new_id,
        "description": description,
        "status": "todo",
        "createdAt": now,
        "updatedAt": now
    }

    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_id})")

def list_tasks(filter_status=None):
    tasks = load_tasks()
    if filter_status:
        tasks = [t for t in tasks if t["status"] == filter_status]

    if len(tasks) == 0:
        print("No tasks found.")
        return

    for task in tasks:
        print(f"[{task['id']}] {task['description']} - {task['status']} (Updated: {task['updatedAt']})")

def update_task(task_id, new_description):
    tasks = load_tasks()
    found = False
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            found = True
            break

    if not found:
        print(f"Task with ID {task_id} not found.")
        return

    save_tasks(tasks)
    print(f"Task {task_id} updated successfully.")

def delete_task(task_id):
    tasks = load_tasks()
    updated_tasks = [task for task in tasks if task["id"] != task_id]

    if len(tasks) == len(updated_tasks):
        print(f"Task with ID {task_id} not found.")
        return

    save_tasks(updated_tasks)
    print(f"Task {task_id} deleted successfully.")

# Add these two functions if you want mark-in-progress / mark-done
def mark_in_progress(task_id):
    tasks = load_tasks()
    found = False
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "in-progress"
            task["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            found = True
            break
    if not found:
        print(f"Task {task_id} not found.")
        return
    save_tasks(tasks)
    print(f"Task {task_id} marked as in-progress.")

def mark_done(task_id):
    tasks = load_tasks()
    found = False
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "done"
            task["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            found = True
            break
    if not found:
        print(f"Task {task_id} not found.")
        return
    save_tasks(tasks)
    print(f"Task {task_id} marked as done.")



                


