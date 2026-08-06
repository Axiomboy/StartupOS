import json

TASK_FILE = "data/tasks.json"


def load_tasks():
    with open(TASK_FILE, "r") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=4)


def add_task(task):
    tasks = load_tasks()

    tasks.append({
        "task": task,
        "status": "Todo"
    })

    save_tasks(tasks)