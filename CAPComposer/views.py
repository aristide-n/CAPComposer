from django.shortcuts import render
from cap import caplib

capMsg = caplib.Alert()
infoBlock = caplib.Info()

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
    # info
    infoBlock._urgency = request.POST['urgency']
    infoBlock._severity = request.POST['severity']
    infoBlock._certainty = request.POST['certainty']
    infoBlock._category = request.POST['category']
    infoBlock._response_type = request.POST['responseType']
    infoBlock._language = request.POST['language']
    infoBlock._event = request.POST['event']
    infoBlock._event = request.POST['event']
    infoBlock._sender_name = request.POST['senderName']
    infoBlock._headline = request.POST['headline']
    infoBlock._description = request.POST['description']
    infoBlock._instruction = request.POST['instruction']
    infoBlock._web = request.POST['web']
    infoBlock._contact = request.POST['contact']
    infoBlock._event_code = request.POST['eventCode']

    capMsg.add_info(infoBlock.to_xml_tree())

    try:
        result = capMsg.to_xml_string()
    except AssertionError as ex:
        result = ex.message

    return render(request, 'finish.html', {'result': result})