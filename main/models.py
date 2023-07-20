from django.contrib.auth.models import User
from django.db import models


class Banner(models.Model):
    image = models.ImageField(upload_to='images/')
    text = models.TextField()

    def __str__(self):
        return self.text


class Category(models.Model):
    name = models.CharField(max_length=123)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=123)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=222)
    created_at = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='images/')
    image_2 = models.ImageField(upload_to='images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=123)
    email = models.CharField(max_length=123)
    website = models.URLField()
    message = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=123)
    email = models.CharField(max_length=123)
    website = models.URLField()
    message = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
