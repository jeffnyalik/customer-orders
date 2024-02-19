from django.urls import path
from .views import SnippetsApiViews, index

urlpatterns = [
    path("Snippets-list/", SnippetsApiViews.as_view(), name="Snippets-list"),
    path("messages/", index, name="messages")
]
