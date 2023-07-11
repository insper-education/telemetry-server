#!/usr/bin/env python3

from .models import *
from django.utils.crypto import get_random_string
import datetime
import json


def studentLoginGH(response):
    userinfo = response["userinfo"]
    if not Student.objects.filter(email=userinfo["email"]):
        token = get_random_string(length=64)
        student = Student.objects.create(token=token)
        student.nickname = userinfo["nickname"]
        student.name = userinfo["name"]
        student.email = userinfo["email"]
        student.picture = userinfo["picture"]
        student.save()
    else:
        student = Student.objects.get(email=userinfo["email"])

    return student.token


def userFromToken(token):
    if len(Student.objects.filter(token=token)) == 0:
        return None
    else:
        return Student.objects.get(token=token)


def checkCourseExists(name):
    if len(Course.objects.filter(name=name)) == 0:
        return False
    else:
        return True


def checkChannelExists(name):
    if len(Channel.objects.filter(name=name)) == 0:
        return False
    else:
        return True


def createCourse(name):
    course = Course.objects.create(name=name)
    course.Professor = None
    course.save()


def createChannel(name):
    channel = Channel.objects.create(name=name)
    channel.save()


def courseFromName(name):
    return Course.objects.get(name=name)


def channelFromName(name):
    return Channel.objects.get(name=name)


def saveTelemetry(student, course, channel, log):
    d = Data(student=student)
    d.course = course
    d.channel = channel
    d.ts = datetime.datetime.now()
    d.log = json.dumps(log, indent=4)
    d.save()
