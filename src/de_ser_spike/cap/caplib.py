__author__ = 'Aristide'
__version__ = '1.0'


from cap.cap_xmlutil import element, add_child, stringify
from uuid import uuid4
"""This module is the collection of classes that represent the CAP 1.2 data dictionary:
http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2-os.html
"""

class Alert(object):

    def __init__(self):
        self._identifier = str(uuid4())     # Generate a random UUID
        self._sender = ''
        self._sent = ''
        self._status = None
        self._msg_type = None
        self._scope = None
        self._info = None


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


    def add_info(self,info_obj):
        """
        TODO: think about how to use cap_xmlutil to append the element
        """
        NotImplemented


    def to_xml_tree(self):
        """
        Convert this alert to element tree format. Return the top element of this `Alert`
        """
        alert = element('alert')

        add_child(alert, self._identifier, 'identifier')
        add_child(alert, self._sender, 'sender')
        add_child(alert, self._sent, 'sent')
        add_child(alert, self._status, 'status')
        add_child(alert, self._msg_type, 'msgType')
        add_child(alert, self._scope, 'scope')

        return alert


    def to_xml_string(self):
        """
        Convert this alert to xml string format. Return the formatted xml string
        """
        return stringify(self.to_xml_tree())



class Info:

    def __init__(self):
        NotImplemented


    def add_area(self, area_obj):
        NotImplemented


    def add_resource(self, resource_obj):
        NotImplemented



class Area:

    def __init__(self):
        NotImplemented


    def add_circle(self, circle_obj):
        NotImplemented


    def add_polygon(self, polygon_obj):
        NotImplemented



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
