from django.shortcuts import render
from cap import caplib
import lxml

capMsg = caplib.Alert()

def alert(request):
    return render(request, 'alert.html')

def map(request):
    capMsg.sender = request.POST['source']
    capMsg.status = request.POST['messageStatus']
    capMsg.msg_type = request.POST['messageType']
    capMsg.scope = request.POST['scope']

    if (capMsg._scope == 'Restricted'):
        capMsg.restriction = request.POST['restrictedText']
    elif(request.POST['scope'] == 'Private'):
        capMsg.address = request.POST['address']

    return render(request, 'map.html')

def info(request):
    return render(request, 'info.html')

def finish(request):
    try:
        result = capMsg.to_xml_string()
    except AssertionError as ex:
        result = ex.message

    return render(request, 'finish.html', {'result': result})