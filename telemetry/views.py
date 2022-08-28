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
        payload = json.loads(request.body)

        student = userFromToken(payload["userToken"])
        courseName = payload["courseName"]
        channel = payload["channel"]
        data = payload["telemetry"]

        if student == None:
            HttpResponse("<h1>No user </h1>", status=400)

        if courseName == None:
            HttpResponse("<h1>No course token</h1>", status=400)

        if not checkCourseExists(courseName):
            createCourse(courseName)

        course = courseFromName(courseName)
        saveTelemetry(student, course, channel, data)
        return HttpResponse(status=200)
    else:
        return HttpResponse("<h1>Send data here.</h1>")


def infoFromToken(request):
    if request.method == "GET":
        token = request.GET.get("token", "")
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
