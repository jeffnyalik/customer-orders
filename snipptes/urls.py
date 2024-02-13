from django.urls import path
from .views import SnippetsApiViews

urlpatterns = [
    path("snippets/", SnippetsApiViews.as_view(), name="snippets")
]
