__author__ = 'Aristide'

import copy
from BeautifulSoup import BeautifulSoup
from nose.tools import assert_raises, assert_raises_regexp, assert_equal, assert_true
from unittest import TestCase

from cap.caplib import Alert

class TestCAPLib(TestCase):

    def setUp(self):
        """
        Initialize a new Alert object
        """
        self.alert = Alert()

        # Set all of alert's required attributes
        self.alert.set_sender('KSTO@NWS.NOAA.GOV')
        self.alert.set_status('Actual')
        self.alert.set_msg_type('Alert')
        self.alert.set_scope('Public')


    # Test converting invalid alert objects to XML

    def test_empty_alert_to_xml(self):
        """
        Try to call alert.to_xml_string for an empty alert object
        """
        self.alert.__init__()
        assert_raises_regexp(AssertionError,'Alert sender is empty string.', self.alert.to_xml_string)


    def test_alert_without_sender_to_xml(self):
        """
        Try to call alert.to_xml_string for an alert missing the sender attribute
        """
        self.alert.set_sender('')
        assert_raises_regexp(AssertionError,'Alert sender is empty string.', self.alert.to_xml_string)


    def test_alert_without_status_to_xml(self):
        """
        Try to call alert.to_xml_string for an alert missing the status attribute
        """
        self.alert.set_status(None)
        assert_raises_regexp(AssertionError,'Alert status is None.', self.alert.to_xml_string)


    def test_alert_without_msg_type_to_xml(self):
        """
        Try to call alert.to_xml_string for an alert missing the msg_type attribute
        """
        self.alert.set_msg_type(None)
        assert_raises_regexp(AssertionError,'Alert message type is None.', self.alert.to_xml_string)


    def test_alert_without_scope_to_xml(self):
        """
        Try to call alert.to_xml_string for an alert missing the scope attribute
        """
        self.alert.set_scope(None)
        assert_raises_regexp(AssertionError,'Alert scope is None.', self.alert.to_xml_string)

    def test_private_alert_without_addresses_to_xml(self):
        """
        Try to call alert.to_xml_string for a private alert missing the addresses attribute
        """
        self.alert.set_scope('Private')
        assert_raises_regexp(AssertionError,'Private Alert doesn\'t have addresses.', self.alert.to_xml_string)

    def test_restricted_alert_without_restriction_to_xml(self):
        """
        Try to call alert.to_xml_string for a restricted alert missing the restriction attribute
        """
        self.alert.set_scope('Restricted')
        assert_raises_regexp(AssertionError,'Restricted Alert doesn\'t have restriction.', self.alert.to_xml_string)


    # Test converting valid alert objects to XML

    def test_valid_alert_to_xml(self):
        """
        Compare the string representations of a valid Alert object to the expected xml strings
        """

        # The reference XML
        valid_xml = '<alert xmlns="urn:oasis:names:tc:emergency:cap:1.2">' \
                    '<identifier>id</identifier>' \
                    '<sender>KSTO@NWS.NOAA.GOV</sender>' \
                    '<sent>time</sent>' \
                    '<status>Actual</status>' \
                    '<msgType>Alert</msgType>' \
                    '<scope>Public</scope>' \
                    '</alert>'

        # Get the XML string representation of alert
        alert_xml = self.alert.to_xml_string(is_formatted=False)

        # Put the alert's XML through beautiful soup to make the "sent" time and "identifier" values the same as
        # the reference XML
        alert_soup = BeautifulSoup(alert_xml)

        alert_soup.identifier.string = 'id'
        alert_soup.sent.string = 'time'

        # Beautiful soup makes the "msgType" tag all lowercase. Restore it to the original form
        alert_soup.msgtype.name = 'msgType'

        # Compare the strings
        assert_equal(str(alert_soup), valid_xml)


        #TODO: Test all required attr for 'Private' scope, i.e add addresses
        #TODO: Test all required attr for 'Restricted' scope, i.e add restriction
        #TODO: Test formatted output
