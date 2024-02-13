from django.db import models


class Snippets(models.Model):
    name = models.CharField(blank=True, null=True, max_length=200)
    
    def __str__(self) -> str:
        return self.name
    