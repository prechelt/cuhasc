from django.test import TestCase
import os


class ReadmeEndingTest(TestCase):
    def test_readme_ends_with_good_ending(self):
        readme_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'README.md')
        with open(readme_path) as f:
            content = f.read()
        self.assertTrue(content.rstrip('\n').endswith("This is a really good ending."))
