from django.db import models


class Grade(models.Model):
    grade = models.IntegerField()
    age = models.IntegerField()


class Classroom(models.Model):
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    number = models.IntegerField()


class Student(models.Model):
    name = models.CharField(max_length=20)
