__author__ = 'Aristide'
__version__ = '0.1'


from lxml import etree

"""This is a thin CAP specific API on top  of lxml. It allows intuitive insertion of alert data into the Alert object's
Element Tree, which then can be serialized to XML.
"""

class Alert:
    def __init__(self):
        None

    def add_info(self,info_obj):
        None


class Info:
    def __initi__(self):
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
