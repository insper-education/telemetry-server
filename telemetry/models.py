from django.db import models
from django.utils.crypto import get_random_string


class Student(models.Model):
    nickname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    picture = models.URLField(max_length=200)
    token = models.CharField(max_length=64)


class Professor(models.Model):
    nickname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    picture = models.URLField(max_length=200)
    token = models.CharField(max_length=64)


class Course(models.Model):
    name = models.CharField(max_length=30)
    professor = models.ForeignKey(
        Professor, on_delete=models.CASCADE, blank=True, null=True
    )


class Data(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    channel = models.CharField(max_length=30)
    #    ts = models.DateTimeField()
    log = models.JSONField()
