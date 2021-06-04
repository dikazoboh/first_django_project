from django.db import models
from datetime import datetime

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=400)
    
    def __str__(self) -> str:
        return self.name

class Faculty(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=100)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

class Grade(models.Model):
    type = models.IntegerField()

    def __str__(self) -> str:
        return self.type

class CertificateType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Student(models.Model):
    School = models.ForeignKey(School, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=40)
    year_of_graduation=models.DateField(default=datetime.today)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    certificate_type = models.ForeignKey(CertificateType, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.fullname







