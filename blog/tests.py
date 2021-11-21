from django.test import TestCase
from blog.models import ArticleModel
from datetime import datetime
from django.utils import timezone


class BlogTests(TestCase):
    def test_article_created_success(self):
        article = ArticleModel.objects.create(title='Test', category='test', author='Fuckhead',
                                              content='test content',
                                              created_at=datetime.now(tz=timezone.utc))
        article.save()
        result = ArticleModel.objects.get(title='Test')
        self.assertEqual(result, article)


class BlogPagesTest(TestCase):
    def test_home_page_content(self):
        result = self.client.get("/blog/")
        self.assertEqual(result.content, b"Welcome to the blog, poo-bum")
