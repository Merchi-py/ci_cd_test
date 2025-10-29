from django.test import TestCase
from .models import Post

class PostTest(TestCase):
    def test_post(self):
        post = Post.objects.create(title="Hello", content="Hello World")
        self.assertEqual(post.title, "Hello")
