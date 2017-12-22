#!/usr/bin/env python

import unittest
from M800Api import M800Api

class M800ApiTest(unittest.TestCase):

    key = '<put your developer key here>';
    secret = '<put your developer secret here>';
    host = 'api.m800.com';
    port = 443;
    sender = '<sender phone number>';
    to = '<recipient phone number>';
    msg = 'Python API client test message.';

    def test_send_sms(self):

        request = {
            'from': self.sender,
            'type': 'text',
            'messageClass': 'normal',
            'body': self.msg
        }

        api = M800Api(self.key, self.secret, self.host, self.port);
        response = api.send_sms(self.to, request)
        print response

    def test_send_text_sms(self):

        api = M800Api(self.key, self.secret, self.host, self.port);
        response = api.send_text_sms(self.sender, self.to, 'normal', self.msg)
        print response


if __name__ == "__main__":
    test_classes = [ M800ApiTest ]
    for test_class in test_classes:
        temp = str(test_class)
        name = temp.split('.')[-1][:-2]
        print "Start of test for", name
        suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
        unittest.TextTestRunner(verbosity=2).run(suite)
        print "End of test for", name