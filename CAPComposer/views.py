from django.shortcuts import render
from cap import caplib
import json

capMsg = caplib.Alert()


def alert(request):
    return render(request, 'alert.html')

def map(request):
    capMsg.sender = request.POST['source'] if request.POST.has_key('source') else ''
    capMsg.status = request.POST['messageStatus'] if request.POST.has_key('messageStatus') else ''
    capMsg.msg_type = request.POST['messageType'] if request.POST.has_key('messageType') else ''
    capMsg.scope = request.POST['scope'] if request.POST.has_key('scope') else ''

    if (capMsg._scope == 'Restricted'):
        capMsg.restriction = request.POST['restrictedText'] if request.POST.has_key('restrictedText') else ''
    elif(capMsg._scope == 'Private'):
        capMsg.address = request.POST['address'] if request.POST.has_key('address') else ''

    return render(request, 'map.html')

def info(request):
    return render(request, 'info.html')

def finish(request):

    infoBlock = caplib.Info()
    area = caplib.Area()

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
    # infoBlock._event_code = request.POST['eventCode']

    #area
    area._area_description = request.POST['areaDesc']

    circles = request.POST['circleAreas']
    circlesDataList = json.loads(circles)
    area.add_multiple_circles(circlesDataList)

    polygons = request.POST['polygonAreas']
    polygonData = json.loads(polygons)
    area.add_multiple_polygons(polygonData)

    #Nest objects
    infoBlock.add_area(area.to_xml_tree())

    capMsg.add_info(infoBlock.to_xml_tree())

    try:
        result = capMsg.to_xml_string()
    except AssertionError as ex:
        result = ex.message

    return render(request, 'finish.html', {'result': result})