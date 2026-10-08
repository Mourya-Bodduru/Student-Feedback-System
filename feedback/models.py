
from django.db import models

class Student(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password1 = models.CharField(max_length=100)
    reg_no = models.CharField(max_length=20)
    year = models.IntegerField()

    def __str__(self):
        return self.username


class Feedback(models.Model):
    DEPARTMENT_CHOICES = [
        ('CME', 'CME'),
        ('ECE', 'ECE'),
        ('MECH', 'MECH'),
        ('EEE','EEE'),
        ('CIVIL', 'CIVIL'),
    ]

    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    tname = models.CharField(max_length=100)
    sname = models.CharField(max_length=100)
    dept = models.CharField(max_length=100, choices=DEPARTMENT_CHOICES)
    feedback_text = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES)

    def __str__(self):
        return f"Feedback from {self.sname} for {self.tname} ({self.dept})"

class Contact(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length=254)
    message = models.TextField()
    is_resolved = models.BooleanField(default=False)

def __str__(self):
    return self.email
