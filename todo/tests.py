from django.test import TestCase

from .models import Todo

class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.todo = Todo.objects.create(
            title = 'test title',
            body = 'test body'
        )
    
    def test_model_content(self):
        self.assertEqual(self.todo.title, 'test title')
        self.assertEqual(self.todo.body, 'test body')
        self.assertEqual(str(self.todo), 'test title')