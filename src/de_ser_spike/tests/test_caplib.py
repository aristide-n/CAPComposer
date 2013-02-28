__author__ = 'Aristide'

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


    def test_invalid_to_xml(self):
        """
        Try to call alert.to_xml_string for an invalid alert object
        """

        # Empty Alert
        assert_raises_regexp(AssertionError,'Alert sender is empty string.', self.alert.to_xml_string)

        # Alert missing required attributes
        self.alert.set_sender('sender')
        assert_raises_regexp(AssertionError,'Alert status is None.', self.alert.to_xml_string)

        self.alert.set_status('Status')
        assert_raises_regexp(AssertionError,'Alert message type is None.', self.alert.to_xml_string)

        self.alert.set_msg_type('type')
        assert_raises_regexp(AssertionError,'Alert scope is None.', self.alert.to_xml_string)

        # Private alert missing addresses
        self.alert.set_scope('Private')
        assert_raises_regexp(AssertionError,'Private Alert doesn\'t have addresses.', self.alert.to_xml_string)

        # Restricted alert missing restriction
        self.alert.set_scope('Restricted')
        assert_raises_regexp(AssertionError,'Restricted Alert doesn\'t have restriction.', self.alert.to_xml_string)

    def test_valid_to_xml(self):
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

        # Set all of alert's required attributes
        self.alert.set_sender('KSTO@NWS.NOAA.GOV')
        self.alert.set_status('Actual')
        self.alert.set_msg_type('Alert')
        self.alert.set_scope('Public')

        # Get the XML string representation
        alert_xml = self.alert.to_xml_string(is_formatted=False)

        # Put the alert's XML through beautiful soup to make the "sent" time and "identifier" values the same as
        # the reference XML
        alert_soup = BeautifulSoup(alert_xml)

        alert_soup.identifier.string = 'id'
        alert_soup.sent.string = 'time'

        # Beautiful soup makes the "msgType" tag all lowercase. Restore it to the canonical form
        alert_soup.msgtype.name = 'msgType'

        # Compare the strings
        assert_equal(str(alert_soup), valid_xml)


        #TODO: Test all required attr for 'Private' scope, i.e add addresses
        #TODO: Test all required attr for 'Restricted' scope, i.e add restriction
        #TODO: Test formatted output
