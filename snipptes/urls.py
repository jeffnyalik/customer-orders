from django.urls import path
from .views import SnippetsApiViews

urlpatterns = [
    path("Snippets-list/", SnippetsApiViews.as_view(), name="Snippets-list")
]
