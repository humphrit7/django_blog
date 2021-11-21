from django.db import models


class ArticleModel(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField()

    def __str__(self):
        return f"{self.id}: {self.title}"
