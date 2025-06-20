from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    context = {
        "title" : "🫎 Jean Moïse TALEC's Website",
        "navbar" : [
            ("ExpressMpeg", "expressmpeg.home"),
            ("Vizysound", "vizysound.home"),
            ("Lambda Course", "lambda_course.home"),
        ],
    }
    return render(request, "main/home.html", context)