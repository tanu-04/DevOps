import unittest
from to_do import add_task, Task, view_tasks, complete_task
import datetime

class TestTodoListFunctions(unittest.TestCase):

    def test_add_task(self):
        todo_list = []
        add_task(todo_list, "Walk the dog")
        self.assertEqual(len(todo_list), 1)
        self.assertEqual(todo_list[0].description, "Walk the dog")
        self.assertIsNone(todo_list[0].due_date)
        self.assertEqual(todo_list[0].estimated_time, 0)
        self.assertFalse(todo_list[0].completed)

        add_task(todo_list, "Pay bills", "2025-04-15", 30)
        self.assertEqual(len(todo_list), 2)
        self.assertEqual(todo_list[1].description, "Pay bills")
        self.assertEqual(todo_list[1].due_date, datetime.date(2025, 4, 15))
        self.assertEqual(todo_list[1].estimated_time, 30)
        self.assertFalse(todo_list[1].completed)

    def test_task_initialization(self):
        task1 = Task("Read a book")
        self.assertEqual(task1.description, "Read a book")
        self.assertIsNone(task1.due_date)
        self.assertEqual(task1.estimated_time, 0)
        self.assertFalse(task1.completed)

        task2 = Task("Submit report", "2025-04-11", 90)
        self.assertEqual(task2.description, "Submit report")
        self.assertEqual(task2.due_date, datetime.date(2025, 4, 11))
        self.assertEqual(task2.estimated_time, 90)
        self.assertFalse(task2.completed)

        task3 = Task("Invalid Date", "invalid-date")
        self.assertIsNone(task3.due_date)

    def test_mark_complete(self):
        task = Task("Complete me")
        task.mark_complete()
        self.assertTrue(task.completed)

    #def test_view_tasks(self, capsys):
    #    todo_list = [
    #        Task("Task 1", "2025-04-12"),
    #        Task("Task 2", estimated_time=60),
    #        Task("Task 3", "2025-04-10", 15),
    #    ]
    #    view_tasks(todo_list)
    #    captured = capsys.readouterr()
    #    self.assertIn("Task 1", captured.out)
    #    self.assertIn("Task 2", captured.out)

    #    view_tasks([], sort_by = 'due')
    #    captured = capsys.readouterr()
    #    self.assertIn("Your to-do list is empty.", captured.out)

    #def test_complete_task(self, capsys):
    #    todo_list = [Task("Task 1"), Task("Task 2")]
    #    complete_task(todo_list, 0)
    #    self.assertTrue(todo_list[0].completed)
    #    complete_task(todo_list, 2)
    #    captured = capsys.readouterr()
    #    self.assertIn("Invalid task index.", captured.out)