from django.forms import ModelForm
from .models import ArticleModel


class ArticleForm(ModelForm):
    class Meta:
        model = ArticleModel
        exclude = ["created_at"]
