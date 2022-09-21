from django.db import models
from django.contrib.auth.models import User
# Create your models here.

GRADES = (
    
    (1, 'Grade 1'),
    (2, 'Grade 2'),
    (3, 'Grade 3'),
    (4, 'Grade 4'),
    (5, 'Grade 5'),
    (6, 'Grade 6'),
    (7, 'Grade 7'),
    (8, 'Grade 8'),
    (9, 'Grade 9'),
    (10, 'Grade 10'),
    (11, 'Grade 11'),
    (12, 'Grade 12'),
    
    )

SECTIONS = (

    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
)

    


class Student(models.Model):
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=150)
    grade = models.IntegerField(choices=GRADES)
    section = models.CharField(max_length=50, choices=SECTIONS)
    score = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    contact = models.CharField(max_length=150)
    

    def __str__(self):
        return self.name