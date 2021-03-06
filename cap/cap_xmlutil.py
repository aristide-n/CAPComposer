__author__ = 'Aristide'


"""This module is a thin CAP specific API on top  of lxml. It allows intuitive insertion of data into the Elements of
the Alert object's Element Tree, which then can be serialized to XML.
"""

from lxml import etree

"""
XML namespace definitions
"""

CAP_SCHEMA_VERSION = '1.2'
CAP_NAMESPACE = 'urn:oasis:names:tc:emergency:cap:{}'.format(CAP_SCHEMA_VERSION)

NSMAP = {None: CAP_NAMESPACE}

"""
Some utility functions for lxml operations
"""

def create_element(name):
    """
    Create an element in the CAP namespace
    """
    return etree.Element("{{{}}}{}".format(CAP_NAMESPACE, name), nsmap=NSMAP)


def add_child(parent, text, name, call=lambda x: x):
    """
    Helper method to add a child if text is not None
    """
    if text is not None:
        tmp = create_element(name)
        tmp.text = call(text)
        parent.append(tmp)


def add_attribute(element, attribute, name, call=lambda x: x):
    """
    Helper method to add an attribute if attr is not None
    """
    if attribute is not None:
        element.attrib[name] = call(attribute)


def stringify(element_, is_formatted=True):
    """
    Helper method to print the xml string representation of the element
    """
    return etree.tostring(element_, pretty_print=is_formatted)


__all__ = ['create_element', 'add_child', 'add_attribute', 'stringify']