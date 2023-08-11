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
        student = userFromToken(token)
        if student == None:
            return HttpResponse(status=401)

        payload = json.loads(request.body)
        courseName = payload["course"]
        channelName = payload["channel"]
        data = payload["log"]

        if student == None:
            HttpResponse("<h1>No user </h1>", status=400)

        if courseName == None:
            HttpResponse("<h1>No course token</h1>", status=400)

        if not checkCourseExists(courseName):
            createCourse(courseName)

        if not checkChannelExists(channelName):
            createChannel(channelName)

        course = courseFromName(courseName)
        channel = channelFromName(channelName)
        saveTelemetry(student, course, channel, data)
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
