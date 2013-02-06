__author__ = 'Aristide'

"""
XML namespace definitions
"""

CAP_SCHEMA_VERSION = '1.2'
EEML_NAMESPACE = 'urn:oasis:names:tc:emergency:cap:{}'.format(CAP_SCHEMA_VERSION)

NSMAP = {None: EEML_NAMESPACE}

"""
Some utility functions for xml operations
"""

from lxml import etree

def element(name):
    """
    Create an element in the EEML namespace
    """
    return etree.Element(name, nsmap=NSMAP)


def addChild(parent, attr, name, call=lambda x: x):
    """
    Helper method to add child if not None
    """
    if attr is not None:
        tmp = element(name)
        tmp.text = call(attr)
        parent.append(tmp)


def addAttribute(elem, attr, name, call=lambda x: x):
    """
    Helper method to add attribute if not None
    """
    if attr is not None:
        elem.attrib[name] = call(attr)

def stringify(elem, is_formatted=True):
    """
    Helper method to print the xml string representation of the element
    """
    return etree.tostring(elem, pretty_print=is_formatted)