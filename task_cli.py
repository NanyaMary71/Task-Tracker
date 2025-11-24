import sys
from task_manager import add_task, list_tasks, update_task, delete_task, mark_in_progress, mark_done


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python task_cli.py <command> [arguments]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Error: Please provide a task description.")
        else:
            description = " ".join(sys.argv[2:])
            add_task(description)

    elif command == "list":
        if len(sys.argv) == 2:
            list_tasks()  # list all
        else:
            status = sys.argv[2]
            valid_status = ["todo", "done", "in-progress"]
            if status not in valid_status:
                print("Error: Status must be todo, done, or in-progress")
            else:
                list_tasks(status)

    elif command == "update":
        if len(sys.argv) < 4:
            print("Usage: python task_cli.py update <id> <new description>")
        else:
            try:
                task_id = int(sys.argv[2])
                new_description = " ".join(sys.argv[3:])
                update_task(task_id, new_description)
            except ValueError:
                print("Error: Task ID must be a number.")
 
    elif command == "delete":
        if len(sys.argv) < 3:
            print("Usage: python task_cli.py delete <id>")
        else:
            try:
                task_id = int(sys.argv[2])
                delete_task(task_id)
            except ValueError:
                print("Error: Task ID must be a number.")

    elif command == "mark-in-progress":
      if len(sys.argv) < 3:
        print("Usage: python task_cli.py mark-in-progress <id>")
      else:
          try:
              task_id = int(sys.argv[2])
              mark_in_progress(task_id)
          except ValueError:
            print("Error: Task ID must be a number.")

    elif command == "mark-done":
      if len(sys.argv) < 3:
        print("Usage: python task_cli.py mark-done <id>")
      else:
        try:
            task_id = int(sys.argv[2])
            mark_done(task_id)
        except ValueError:
            print("Error: Task ID must be a number.")

