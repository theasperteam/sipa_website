from django.db import models

# Create your models here.
class Contact_Form_Events(models.Model):
    Name = models.TextField(max_length=100, null=True)
    Email = models.TextField(max_length=70, null=True)
    Phone = models.TextField(max_length=10, null=True)
    Category = models.TextField(max_length=30, null=True)
    Message = models.TextField(max_length=400, null=True)

    def __str__(self):
        return self.Email

class Book_Appointment_Events(models.Model):
    Name = models.TextField(max_length=100, null=True)
    Email = models.TextField(max_length=70, null=True)
    Phone = models.TextField(max_length=10, null=True)
    Category = models.TextField(max_length=30, null=True)

    def __str__(self):
        return self.Email

