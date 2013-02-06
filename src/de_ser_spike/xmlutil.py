__author__ = 'Aristide'
__all__ = ['element', 'add_child', 'stringify']

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


def add_child(parent, attr, name, call=lambda x: x):
    """
    Helper method to add child if not None
    """
    if attr is not None:
        tmp = element(name)
        tmp.text = call(attr)
        parent.append(tmp)


def add_attribute(element_, attr, name, call=lambda x: x):
    """
    Helper method to add attribute if not None
    """
    if attr is not None:
        element_.attrib[name] = call(attr)


def stringify(element_, is_formatted=True):
    """
    Helper method to print the xml string representation of the element
    """
    return etree.tostring(element_, pretty_print=is_formatted)