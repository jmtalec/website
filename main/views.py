from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    context = {
        "title" : "🫎 Jean Moïse TALEC's Website",
    }
    return render(request, "main/home.html", context)