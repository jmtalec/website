from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        "title": "Vizysound",
    }
    return render(request, "vizysound/home.html", context)