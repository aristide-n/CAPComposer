__author__ = 'Aristide'
__version__ = '1.0'


from cap.cap_xmlutil import create_element, add_child, stringify
from uuid import uuid4
from datetime import datetime
from pytz.gae import pytz

"""This module is the collection of classes that represent the CAP 1.2 XML schema:
http://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2-os.html
"""

class Alert(object):

    def __init__(self):
        """
        Initialize the Alert's hidden attributes by set their default values
        """
        self._identifier = str(uuid4())     # Generate a random UUID
        self._sender = ''
        self._sent = ''
        self._status = None
        self._msg_type = None
        self._scope = None
        self._restriction = ''
        self._addresses = []


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


    def set_restriction(self, value):
        """
        Writer method for the _restriction attribute
        """
        self._restriction = value
    restriction = property(fset=set_restriction)


    def set_address(self, value):
        """
        Writer method for items of the _addresses attribute
        """
        self._addresses.append(value)
    address = property(fset=set_address)


    def to_xml_tree(self):
        """
        Convert this alert to XML element tree format. Return the top element of the XML tree
        """

        # Check if required attributes are set
        assert (self._sender is not ''), "Alert sender is empty string."
        assert (self._status is not None), "Alert status is None."
        assert (self._msg_type is not None), "Alert message type is None."
        assert (self._scope is not None), "Alert scope is None."

        # At least one address is required for the private scope
        if self._scope is 'Private':
            assert (self._addresses), "Private Alert doesn't have addresses." # Empty list means False

        # A restriction message is required for the restricted scope
        if self._scope is 'Restricted': assert (self._restriction is not ''), \
                                        "Restricted Alert doesn't have restriction."

        # Create the XML tree
        alert = create_element('alert')
        self._sent = datetime.now(pytz.utc).replace(microsecond=0)

        add_child(alert, self._identifier, 'identifier')
        add_child(alert, self._sender, 'sender')
        add_child(alert, str(self._sent.isoformat()), 'sent')
        add_child(alert, self._status, 'status')
        add_child(alert, self._msg_type, 'msgType')
        add_child(alert, self._scope, 'scope')

        return alert


    def to_xml_string(self, is_formatted=True):
        """
        Convert this alert to xml string format. Return the formatted xml string
        """
        try:
            alert_xml = stringify(self.to_xml_tree(), is_formatted)
        except AssertionError:
            print "The CAP Alert is invalid; aborted generating XML."
            raise # re-raise the exception to give an audit trail to callers of this method.
        else:
            return alert_xml
