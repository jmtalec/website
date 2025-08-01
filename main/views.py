from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    context = {
        "title" : "🫎 Jean Moïse TALEC's Website",
        "navbar" : [
            ("ExpressMpeg", "expressmpeg.home"),
            ("Vizysound", "vizysound.home"),
            ("Lambda_Course", "lambda_course.home"),
        ],
        "projects" : [
            {
                "title" : "ExpressMpeg",
                "description": "That's the tool I've built to convert my audio files to various formats easily.",
                "url" : "expressmpeg.home",
                "image" : "/static/img/logo_moose.png",
            },
            {
                "title" : "Vizysound",
                "description" : "Experimental: shows a glimps of the world of synestesia through sounds and colours...",
                "url" : "vizysound.home",
                "image" : "/static/img/logo_moose.png",
            },
            {
                "title" : "Lambda_Course",
                "description" : "Explores all main concepts of programmation through lambda python syntax.",
                "url" : "lambda_course.home",
                "image" : "/static/img/logo_moose.png",
            }

        ]

    }
    return render(request, "main/home.html", context)