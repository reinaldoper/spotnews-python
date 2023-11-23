from django.db import models
from news.validators import (
    validate_not_single_word, validate_date, validate_content
)


class Category(models.Model):
    name = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=200, null=False)
    password = models.CharField(max_length=200, null=False)
    role = models.CharField(max_length=200, null=False)
    email = models.EmailField(max_length=200, null=False)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=200, null=False,
                             validators=[validate_not_single_word])
    content = models.TextField(null=False, validators=[validate_content],
                               max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(null=False, validators=[validate_date])
    image = models.ImageField(upload_to='img/', blank=True, null=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title
