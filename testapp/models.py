from django.db import models

# Create your models here.
from django.db import models


class Department(models.Model):
    department_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.department_name


class Student(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    mobile = models.IntegerField()


    def __str__(self):
        return self.name