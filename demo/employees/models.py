from django.db import models

# Create your models here.
class Employee(models.Model):
    firstName = models.TextField()
    lastName = models.TextField()
    email = models.TextField()
    phone = models.TextField()
    title = models.TextField()
    department = models.TextField()
    birthdate = models.TextField() 