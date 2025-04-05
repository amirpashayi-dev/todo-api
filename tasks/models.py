from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name


class Todo(models.Model):
    FLAG_CHOICES = (
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    is_done = models.BooleanField(default=False)
    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField(blank=True, null=True)
    flag = models.CharField(choices=FLAG_CHOICES, max_length=10)


    def __str__(self):
        return self.name

    def clean(self):
        if self.end and self.end < self.start:
            raise ValidationError("End date must be after start date")