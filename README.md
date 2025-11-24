https://roadmap.sh/projects/task-tracker
Task Tracker CLI

A simple Command Line Interface (CLI) application to track and manage your tasks. You can add, update, delete, and mark tasks as “in-progress” or “done”. Tasks are stored in a JSON file so your data persists between sessions.

Features

Add new tasks

List all tasks

List tasks by status: todo, in-progress, done

Update task description

Delete tasks

Mark tasks as in-progress or done

Requirements

Python 3.x

No external libraries needed (uses built-in json, os, and datetime)

Installation & Setup

Clone or download this repository.

Navigate to the project folder:

cd path/to/project


Ensure Python is installed:

python --version


Run commands via terminal.

Usage
Add a task
python task_cli.py add "Buy groceries"


Output:

Task added successfully (ID: 1)

List tasks

List all tasks:

python task_cli.py list


List tasks by status:

python task_cli.py list todo
python task_cli.py list in-progress
python task_cli.py list done

Update a task
python task_cli.py update 1 "Buy groceries and cook dinner"

Delete a task
python task_cli.py delete 1

Mark a task as in-progress
python task_cli.py mark-in-progress 1

Mark a task as done
python task_cli.py mark-done 1

Task Properties

Each task has the following properties:

id – Unique identifier

description – Task description

status – Task status: todo, in-progress, done

createdAt – Task creation timestamp

updatedAt – Task last updated timestamp

File Structure
task_tracker/
├── task_cli.py          # CLI interface
├── task_manager.py      # Task management logic
├── tasks.json           # Data storage file (auto-created)
└── README.md

Notes

The tasks.json file is automatically created in the project folder when you run the CLI for the first time.

Error handling is implemented for invalid task IDs or missing inputs.

No external libraries are required — pure Python.

Future Enhancements

Add a graphical user interface (GUI) using Tkinter or PyQt.

Filter tasks by date or search keywords.

Add task priorities or categories.
