from django.shortcuts import render

def alert(request):
    return render(request, 'website/alert.html')

def map(request):
    return render(request, 'website/map.html')

def info(request):
    return render(request, 'website/info.html')

def finish(request):
    return render(request, 'website/finish.html')