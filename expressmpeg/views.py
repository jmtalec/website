from django.shortcuts import render

# Create your views here.

def home(request):
    context = {
        "title": "ExpressMpeg"
    }
    return render(request, "expressmpeg/home.html", context)