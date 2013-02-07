__author__ = 'Aristide'

from lxml import etree
from nose.tools import assert_equal, assert_true
from formencode.doctest_xml_compare import xml_compare
from unittest import TestCase

from cap.cap_xmlutil import element, add_child, add_attribute, stringify

class TestCAPXMLUtil(TestCase):

    def setUp(self):
        self.elem = element('test_elem')


    def test_element(self):
        assert_true(xml_compare(etree.fromstring("""<test_elem xmlns="urn:oasis:names:tc:emergency:cap:1.2"/>"""),
                                self.elem, reporter=self.fail))


    def test_add_child_with_text(self):
        add_child(self.elem, "Child added!", "test_child", lambda x: x+str( len(x) ) )

        assert_true(xml_compare(etree.fromstring(
            """<test_elem xmlns="urn:oasis:names:tc:emergency:cap:1.2">"""
            """<test_child>Child added!12</test_child></test_elem>"""), self.elem, reporter=self.fail))


    def test_add_child_without_text(self):
        add_child(self.elem, None, "test_child", lambda x: x+str( len(x) ) )

        assert_true(xml_compare(etree.fromstring("""<test_elem xmlns="urn:oasis:names:tc:emergency:cap:1.2"/>"""),
                                self.elem, reporter=self.fail))


    def test_add_attribute(self):
        add_attribute(self.elem, "Attribute added!", "test_attr", lambda x: x+str( len(x) ) )

        assert_true(xml_compare(etree.fromstring(
            """<test_elem xmlns="urn:oasis:names:tc:emergency:cap:1.2" test_attr="Attribute added!16"/>"""),
            self.elem, reporter=self.fail))


    def test_add_attribute_without_value(self):
        add_attribute(self.elem, None, "test_attr", lambda x: x+str( len(x) ) )

        assert_true(xml_compare(etree.fromstring(
            """<test_elem xmlns="urn:oasis:names:tc:emergency:cap:1.2"/>"""),
            self.elem, reporter=self.fail))


    def test_stringify_formatted(self):
        add_child(self.elem, "Child added!", "test_child", lambda x: x+str( len(x) ) )

        assert_equal(
            """<test_elem xmlns="urn:oasis:names:tc:emergency:cap:1.2">\n"""
            """  <test_child>Child added!12</test_child>\n</test_elem>\n""",
            stringify(self.elem))


    def test_stringify_non_formatted(self):
        add_child(self.elem, "Child added!", "test_child", lambda x: x+str( len(x) ) )

        assert_equal(
            """<test_elem xmlns="urn:oasis:names:tc:emergency:cap:1.2">"""
            """<test_child>Child added!12</test_child></test_elem>""",
            stringify(self.elem, False))