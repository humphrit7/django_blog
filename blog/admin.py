from django.contrib import admin
from blog.models import ArticleModel


@admin.register(ArticleModel)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_at")
