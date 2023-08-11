from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

from .models import *
from .user import *
import json


@csrf_exempt
def telemetry(request):
    if request.method == "POST":
        token = request.headers.get("Authorization")
<<<<<<< HEAD
        studentData = userFromToken(token)
        if studentData == None:
            return HttpResponse(status=401)

        payload = json.loads(request.body)
        course = payload["course"]
        channel = payload["channel"]
=======
        student = userFromToken(token)
        if student == None:
            return HttpResponse(status=401)

        payload = json.loads(request.body)
        courseName = payload["course"]
        channelName = payload["channel"]
>>>>>>> f7551f5 (improve authorizations)
        data = payload["log"]

        if not checkCourseExists(course):
            createCourse(course)

        if not checkChannelExists(channel):
            createChannel(channel)

        courseData = courseFromName(course)
        channelData = channelFromName(channel)
        saveTelemetry(studentData, courseData, channelData, data)
        return HttpResponse(status=200)
    else:
        return HttpResponse("<h1>Send data here.</h1>")


def infoFromToken(request):
    if request.method == "GET":
        token = request.headers.get("Authorization")
        user = userFromToken(token)
        if user == None:
            return HttpResponse(status=400)
        else:
            json = serializers.serialize(
                "json",
                [
                    user,
                ],
            )

    return HttpResponse(json, content_type="application/json")
