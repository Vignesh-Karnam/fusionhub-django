from django.shortcuts import render

def competitors(request):
    return render(request, 'competitors/competitors.html')
