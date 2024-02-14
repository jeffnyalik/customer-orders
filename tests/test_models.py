from django.test import TestCase
from snipptes.models import Snippets


class SnippetModelTestCase(TestCase):
    def test_Create_snippet(self):
        #Create a snippet instance
        snippet = Snippets.objects.create(name="snipone", code="100abadn")

        #Check if snippet was created successfully
        self.assertIsNotNone(snippet.pk)
        self.assertEqual(snippet.name, "snipone")
        self.assertEqual(snippet.code, "100abadn")
        