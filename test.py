import unittest
from to_do import add_task, Task  # Replace your_module_name
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

if __name__ == '__main__':
    unittest.main()