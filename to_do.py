import datetime

class Task:
    def __init__(self, description, due_date=None, estimated_time=0):
        self.description = description
        self.due_date = self._parse_due_date(due_date)
        self.estimated_time = estimated_time  # in minutes
        self.completed = False

    def _parse_due_date(self, date_str):
        if date_str:
            try:
                return datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
                return None
        return None

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        due = f" (Due: {self.due_date})" if self.due_date else ""
        time_est = f" (Est. Time: {self.estimated_time} mins)" if self.estimated_time else ""
        status = "[X]" if self.completed else "[ ]"
        return f"{status} {self.description}{due}{time_est}"

def add_task(todo_list, description, due_date=None, estimated_time=0):
    task = Task(description, due_date, estimated_time)
    todo_list.append(task)
    print(f"Task '{description}' added.")

def view_tasks(todo_list, sort_by='due'):
    if not todo_list:
        print("Your to-do list is empty.")
        return

    if sort_by == 'due':
        sorted_tasks = sorted(todo_list, key=lambda task: task.due_date if task.due_date else datetime.date.max)
    elif sort_by == 'time':
        sorted_tasks = sorted(todo_list, key=lambda task: task.estimated_time)
    else:
        sorted_tasks = todo_list

    print("\n--- Your To-Do List ---")
    for task in sorted_tasks:
        print(task)
    print("-------------------------\n")

def complete_task(todo_list, index):
    if 0 <= index < len(todo_list):
        todo_list[index].mark_complete()
        print(f"Task '{todo_list[index].description}' marked as complete.")
    else:
        print("Invalid task index.")

# Example Usage (not part of the testable functions)
if __name__ == "__main__":
    my_todos = []
    add_task(my_todos, "Buy groceries", "2025-04-12")
    add_task(my_todos, "Write code", estimated_time=60)
    add_task(my_todos, "Call a friend", "2025-04-10", 15)
    view_tasks(my_todos)
    complete_task(my_todos, 0)
    view_tasks(my_todos, sort_by='time')