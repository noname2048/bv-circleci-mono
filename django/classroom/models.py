from django.db import models
from django.contrib.auth.models import AbstractUser


class School(models.Model):
    name = models.CharField(max_length=20)


class Grade(models.Model):
    age = models.IntegerField()


class Classroom(models.Model):
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    number = models.IntegerField()


class Student(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)


class User(AbstractUser):
    uuid = models.UUIDField(unique=True, db_index=True)
    email = models.CharField(max_length=64, unique=True)


class SchoolStaff(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class GradeStaff(models.Model):
    school_staff = models.ForeignKey(SchoolStaff, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)


class ClassroomStaff(models.Model):
    school_staff = models.ForeignKey(SchoolStaff, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)