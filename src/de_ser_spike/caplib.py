__author__ = 'Aristide'
__version__ = '0.1'


from xmlutil import *

"""This is a thin CAP specific API on top  of lxml. It allows intuitive insertion of alert data into the Alert object's
Element Tree, which then can be serialized to XML.
"""

class Alert:
    def __init__(self):
        self.identifier = None
        self.sender = None
        self.sent = None
        self.status = None
        self.msg_type = None
        self.scope = None
        self.info = None

    def add_info(self,info_obj):
        None

    def to_xml_tree(self):
        """
        Convert this alert to element tree format. Return the top element of this `Alert`
        """
        alert = element('alert')

        add_child(alert, self.identifier, 'identifier')
        add_child(alert, self.sender, 'sender')
        add_child(alert, self.sent, 'sent')
        add_child(alert, self.status, 'status')
        add_child(alert, self.msg_type, 'msgType')
        add_child(alert, self.scope, 'scope')

        return alert

    def to_xml_string(self):
        """
        Convert this alert to xml string format. Return the formatted xml string
        """
        return stringify(self.to_xml_tree())

class Info:
    def __init__(self):
        None

    def add_area(self, area_obj):
        None

    def add_resource(self, resource_obj):
        None


class Area:
    def __init__(self):
        None

    def add_circle(self, circle_obj):
        None

    def add_polygon(self, polygon_obj):
        None


class Circle:
    def __init__(self):
        None


class Polygon:
    def __init__(self):
        None

    def add_point(self, point_obj):
        None


class Point:
    def __init__(self):
        None


class Resource:
    def __init__(self):
        None
