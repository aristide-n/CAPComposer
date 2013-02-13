from django.shortcuts import render
from cap import caplib
import lxml

capMsg = caplib.Alert()

def alert(request):
    return render(request, 'alert.html')

def map(request):

    cap_sender  = request.POST['source']
    cap_status  = request.POST['messageStatus']
    cap_msgType  = request.POST['messageType']
    cap_scope = request.POST['scope']

    capMsg.sender = cap_sender
    capMsg.status = cap_status
    capMsg.msg_type = cap_msgType
    capMsg.scope = cap_scope

    return render(request, 'map.html')

def info(request):
    return render(request, 'info.html')

def finish(request):
    cap_xml = capMsg.to_xml_string()

    return render(request, 'finish.html', {'xml': cap_xml})