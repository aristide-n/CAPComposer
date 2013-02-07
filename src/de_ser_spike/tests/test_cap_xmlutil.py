__author__ = 'Aristide'

from lxml import etree
from nose.tools import assert_equal, assert_true
from formencode.doctest_xml_compare import xml_compare
from unittest import TestCase

from cap.cap_xmlutil import create_element, add_child, add_attribute, stringify

class TestCAPXMLUtil(TestCase):

    def setUp(self):
        self.element = create_element('test_elem')


    def test_element(self):
        assert_true(xml_compare(etree.fromstring("""<test_elem xmlns="urn:oasis:names:tc:emergency:cap:1.2"/>"""),
                                self.element, reporter=self.fail))


    def test_add_child_with_text(self):
        add_child(self.element, "Child added!", "test_child", lambda x: x+str( len(x) ) )

        assert_true(xml_compare(etree.fromstring(
            """<test_elem xmlns="urn:oasis:names:tc:emergency:cap:1.2">"""
            """<test_child>Child added!12</test_child></test_elem>"""), self.element, reporter=self.fail))


    def test_add_child_without_text(self):
        add_child(self.element, None, "test_child", lambda x: x+str( len(x) ) )

        assert_true(xml_compare(etree.fromstring("""<test_elem xmlns="urn:oasis:names:tc:emergency:cap:1.2"/>"""),
                                self.element, reporter=self.fail))


    def test_add_attribute(self):
        add_attribute(self.element, "Attribute added!", "test_attr", lambda x: x+str( len(x) ) )

        assert_true(xml_compare(etree.fromstring(
            """<test_elem xmlns="urn:oasis:names:tc:emergency:cap:1.2" test_attr="Attribute added!16"/>"""),
            self.element, reporter=self.fail))


    def test_add_attribute_without_value(self):
        add_attribute(self.element, None, "test_attr", lambda x: x+str( len(x) ) )

        assert_true(xml_compare(etree.fromstring(
            """<test_elem xmlns="urn:oasis:names:tc:emergency:cap:1.2"/>"""),
            self.element, reporter=self.fail))


    def test_stringify_formatted(self):
        add_child(self.element, "Child added!", "test_child")

        assert_equal(
            """<test_elem xmlns="urn:oasis:names:tc:emergency:cap:1.2">\n"""
            """  <test_child>Child added!</test_child>\n</test_elem>\n""",
            stringify(self.element))


    def test_stringify_non_formatted(self):
        add_child(self.element, "Child added!", "test_child")

        assert_equal(
            """<test_elem xmlns="urn:oasis:names:tc:emergency:cap:1.2">"""
            """<test_child>Child added!</test_child></test_elem>""",
            stringify(self.element, False))