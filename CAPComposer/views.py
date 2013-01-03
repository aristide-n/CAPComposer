from django.shortcuts import render

def alert(request):
    return render(request, 'alert.html')

def map(request):
    return render(request, 'map.html')

def info(request):
    return render(request, 'info.html')

def finish(request):
    return render(request, 'finish.html')