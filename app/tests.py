from django.test import TestCase
from .models import *


# Create your tests here.
class TestProfile(TestCase):
    def setUp(self):
        self.user = User(id=1, username='iano', password='sang')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()


class PostTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='charles')
        self.post = Post.objects.create(id=1, title='test post', photo='', description='description', user=self.user,
                                        url='http://127.0.0.1:8000/index/')

    def test_instance(self):
        self.assertTrue(isinstance(self.post, Post))

    def test_save_post(self):
        self.post.save_post()
        post = Post.objects.all()
        self.assertTrue(len(post) > 0)

    def test_get_posts(self):
        self.post.save()
        posts = Post.all_posts()
        self.assertTrue(len(posts) > 0)

    def test_search_post(self):
        self.post.save()
        post = Post.search_project('test')
        self.assertTrue(len(post) > 0)

    def test_delete_post(self):
        self.post.delete_post()
        post = Post.search_project('test')
        self.assertTrue(len(post) < 1)


class RatingTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='charles')
        self.post = Post.objects.create(id=1, title='test post', photo='photo.url',description='description',
                                        user=self.user, url='http://127.0.0.1:8000/index/')
        self.rating = Rating.objects.create(id=1, design=9, usability=8, content=7, user=self.user, post=self.post)

    def test_instance(self):
        self.assertTrue(isinstance(self.rating, Rating))

    def test_save_rating(self):
        self.rating.save_rating()
        rating = Rating.objects.all()
        self.assertTrue(len(rating) > 0)


