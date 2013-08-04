__author__ = 'Aristide'
__version__ = '1.0'

from cap.cap_xmlutil import create_element, add_child, stringify
from uuid import uuid4
from datetime import datetime
from pytz.gae import pytz
import xmlsec

"""This module is the collection of classes that represent the CAP 1.2 XML schema:
http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2-os.html
"""


class Alert(object):
    def __init__(self):
        """
        Initialize the Alert's hidden attributes by set their default values
        """
        self._identifier = str(uuid4())     # Generate a random UUID
        self._sender = ''
        self._sent = ''
        self._status = None
        self._msg_type = None
        self._scope = None
        self._restriction = ''
        self._addresses = []
        self._info = None
        self._signature = None


    def set_sender(self, value):
        """
        Writer method for the _sender attribute
        """
        self._sender = value

    sender = property(fset=set_sender)


    def set_status(self, value):
        """
        Writer method for the _status attribute
        """
        self._status = value

    status = property(fset=set_status)


    def set_msg_type(self, value):
        """
        Writer method for the _msg_type attribute
        """
        self._msg_type = value

    msg_type = property(fset=set_msg_type)


    def set_scope(self, value):
        """
        Writer method for the _scope attribute
        """
        self._scope = value

    scope = property(fset=set_scope)


    def set_restriction(self, value):
        """
        Writer method for the _restriction attribute
        """
        self._restriction = value

    restriction = property(fset=set_restriction)


    #TODO: refactor for multiple addresses
    def set_address(self, value):
        """
        Writer method for the _restriction attribute
        """
        self._addresses.append(value)

    address = property(fset=set_address)


    def add_info(self, info_tree):
        """
        """
        #TODO: think about how to use cap_xmlutil to append the element
        self._info = info_tree


    def to_xml_tree(self):
        """
        Convert this alert to element tree format. Return the top element of the Alert tree
        """

        # Check if required attributes are set
        assert (self._sender not in ['', None]), "Alert sender is empty string."
        assert (self._status is not None), "Alert status is None."
        assert (self._msg_type is not None), "Alert message type is None."
        assert (self._scope is not None), "Alert scope is None."

        # A restriction message is required for the restricted scope
        if self._scope == 'Restricted':
            assert (self._restriction not in ['', None]), "Restricted Alert doesn't have restriction."

        # At least one address is required for the private scope
        if self._scope == 'Private':
            assert (any(self._addresses)), "Private Alert doesn't have addresses."

        # Create the XML tree
        alert = create_element('alert')
        self._sent = datetime.now(pytz.utc).replace(microsecond=0)

        add_child(alert, self._identifier, 'identifier')
        add_child(alert, self._sender, 'sender')
        add_child(alert, str(self._sent.isoformat()), 'sent')
        add_child(alert, self._status, 'status')
        add_child(alert, self._msg_type, 'msgType')
        add_child(alert, self._scope, 'scope')
        if self._scope == 'Restricted': add_child(alert, self._restriction, 'restriction')
        if self._scope == 'Private': add_child(alert, self._addresses.pop(), 'addresses')
        if self._info is not None: alert.append(self._info)
        if self._signature is not None: alert.append(self._signature)

        return alert


    def to_xml_string(self, is_formatted=True):
        """
        Convert this alert to xml string format. Return the formatted xml string
        """
        try:
            alert_xml = stringify(self.to_xml_tree(), is_formatted)
        except AssertionError:
            raise # re-raise the exception to give an audit trail to callers of this method.
        else:
            return alert_xml


    def add_signature(self, private_key_path, public_cert_path):
        NotImplemented
        #Verify the key path
        #Verify the cert path
        #Make sure that _signature is None
        #Generate signature with xmlsec
        #extract the signature from the returned tree,
        #save it at _signature
        #return


    def verify_signature(self, public_cert_path):
        NotImplemented
        #If there is a signature
        #verify the cert path
        #verify using xmlsec
        #and return


class Info:
    def __init__(self):
        self._urgency = ''
        self._severity = ''
        self._certainty = ''
        self._category = ''
        self._response_type = ''
        self._language = ''
        self._event = ''
        self._sender_name = ''
        self._headline = ''
        self._description = ''
        self._instruction = ''
        self._web = ''
        self._contact = ''
        self._event_code = None
        self._area = None


    def set_urgency(self, value):
        self._urgency = value

    urgency = property(fset=set_urgency)


    def add_area(self, area_tree):
        self._area = area_tree


    def add_resource(self, resource_obj):
        NotImplemented


    def to_xml_tree(self):
        info = create_element('info')

        add_child(info, self._language, 'language')
        add_child(info, self._category, 'category')
        add_child(info, self._event, 'event')
        add_child(info, self._response_type, 'responseType')
        add_child(info, self._urgency, 'urgency')
        add_child(info, self._severity, 'severity')
        add_child(info, self._certainty, 'certainty')

        if self._event_code:
            event_code_text = self._event_code.split(':')
            event_code = create_element('eventCode')
            add_child(event_code, event_code_text[0], 'valueName')
            add_child(event_code, event_code_text[1], 'value')

            info.append(event_code)

        add_child(info, self._sender_name, 'senderName')
        add_child(info, self._headline, 'headline')
        add_child(info, self._description, 'description')
        add_child(info, self._instruction, 'instruction')
        add_child(info, self._web, 'web')
        add_child(info, self._contact, 'contact')

        if self._area is not None: info.append(self._area)

        return info


class Area:
    def __init__(self):
        self._area_description = ''
        self._polygons = []
        self._circles = []


    def add_multiple_circles(self, circle_points_list):
        i = 0

        while i < len(circle_points_list):
            center_lat = circle_points_list[i]
            center_long = circle_points_list[i + 1]
            radius = circle_points_list[i + 2]

            # Add the circle
            self.add_circle(center_lat, center_long, radius)

            # Increment the iterator
            i += 3


    def add_multiple_polygons(self, polygons_list):
        for polygon in polygons_list:
            self.add_polygon(polygon)


    def add_circle(self, center_lat, center_long, radius):
        circle_str = str(center_lat) + ',' + str(center_long) + ' ' + str(radius)
        self._circles.append(circle_str)


    def add_polygon(self, polygon_vertices):
        polygon_str = str(polygon_vertices[0])

        polygon_vertices.append(polygon_vertices[0])
        polygon_vertices.append(polygon_vertices[1])
        polygon_vertices = polygon_vertices[1:]

        for index, vertex in enumerate(polygon_vertices):
            polygon_str += ',' if ((index %2 == 0)) else ' '
            polygon_str += str(vertex)

        self._polygons.append(polygon_str)


    def to_xml_tree(self):
        area = create_element('area')

        add_child(area, self._area_description, 'areaDesc')
        if self._polygons:
            for polygon in self._polygons:
                add_child(area, polygon, 'polygon')

        if self._circles:
            for circle in self._circles:
                add_child(area, circle, 'circle')

        return area


class Circle:
    def __init__(self):
        NotImplemented


class Polygon:
    def __init__(self):
        NotImplemented


    def add_point(self, point_obj):
        NotImplemented


class Point:
    def __init__(self):
        NotImplemented


class Resource:
    def __init__(self):
        NotImplemented
