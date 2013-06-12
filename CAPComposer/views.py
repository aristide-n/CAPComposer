from django.shortcuts import render
from cap import caplib
import json
import xmlsec
import os
from lxml import etree

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
    infoBlock._urgency = request.POST['urgency'] if request.POST.has_key('urgency') else ''
    infoBlock._severity = request.POST['severity'] if request.POST.has_key('severity') else ''
    infoBlock._certainty = request.POST['certainty'] if request.POST.has_key('certainty') else ''
    infoBlock._category = request.POST['category'] if request.POST.has_key('category') else ''
    infoBlock._response_type = request.POST['responseType'] if request.POST.has_key('responseType') else ''
    infoBlock._language = request.POST['language'] if request.POST.has_key('language') else ''
    infoBlock._event = request.POST['event'] if request.POST.has_key('event') else ''
    infoBlock._sender_name = request.POST['senderName'] if request.POST.has_key('senderName') else ''
    infoBlock._headline = request.POST['headline'] if request.POST.has_key('headline') else ''
    infoBlock._description = request.POST['description'] if request.POST.has_key('description') else ''
    infoBlock._instruction = request.POST['instruction'] if request.POST.has_key('instruction') else ''
    infoBlock._web = request.POST['web'] if request.POST.has_key('web') else ''
    infoBlock._contact = request.POST['contact'] if request.POST.has_key('contact') else ''
    # infoBlock._event_code = request.POST['eventCode']

    #area
    area._area_description = request.POST['areaDesc'] if request.POST.has_key('areaDesc') else ''

    circles = request.POST['circleAreas'] if request.POST.has_key('circleAreas') else '{}'
    circlesDataList = json.loads(circles) #if request.POST.has_key('source') else ''
    area.add_multiple_circles(circlesDataList)

    polygons = request.POST['polygonAreas'] if request.POST.has_key('polygonAreas') else '{}'
    polygonData = json.loads(polygons)
    area.add_multiple_polygons(polygonData)

    #Nest objects
    infoBlock.add_area(area.to_xml_tree())

    capMsg.add_info(infoBlock.to_xml_tree())

    #Apply a digital signature

    #Get the private key and the certificate
    datadir = os.path.abspath('./test/data/x509Files')
    private_key = os.path.join(datadir, 'test.pem')
    public_certificate = os.path.join(datadir, 'test.cert')

    #Add the signature and print
    signed_cap_msg = xmlsec.sign(capMsg.to_xml_tree(),
                             key_spec=private_key,
                             cert_spec=public_certificate)

    print etree.tostring(signed_cap_msg, pretty_print=True)

    # Verify and print
    print xmlsec.verify(signed_cap_msg, public_certificate)

    try:
        result = capMsg.to_xml_string()
        # result = signed_cap_msg.to_xml_string()
    except AssertionError as ex:
        result = ex.message

    return render(request, 'finish.html', {'result': result})