from django.db import models
from django.utils import timezone

class Person(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    mobile = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
