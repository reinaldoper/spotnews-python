from django.db import models


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
