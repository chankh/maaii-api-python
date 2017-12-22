"""
This sample code is licensed under the Apache license, with the following
additional copyrights and restrictions:

Copyright 2014 M800

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import hashlib
import hmac
import json
import md5
import time
import urllib2
import urllib
import urlparse


class M800Api(object):

    AUTHENTICATION_SCHEME = "MAAIISDK10"
    CONTENT_MD5_HEADER = "Content-MD5"
    EXPLICIT_DATE = "X-M-Date"
    API_BASE = "/api/1.0"

    def __init__(self, key, secret, host, port):
        """ Constructor that sets up the URL and appropriate credentials
            used to sign HTTP requests. """

        self.key = key
        self.secret = secret
        self.host = host
        self.port = port

        if (port == 443):
            self.scheme = "https"
        else:
            self.scheme = "http"

    def send_text_sms(self, sender, to, message_class, body):
        request = {}
        request['from'] = sender
        request['type'] = 'text'
        request['messageClass'] = message_class
        request['body'] = body

        return self.send_sms(to, request)

    def send_binary_sms(self, sender, to, message_class, body):
        request = {}
        request['from'] = sender
        request['type'] = 'binary'
        request['messageClass'] = message_class
        request['body'] = body

        return self.send_sms(to, request)

    def send_sms(self, to, request):
        resource_uri = "%s/sms/%s" % (M800Api.API_BASE, to)

        payload = json.dumps(request)
        content_md5 = md5.new(payload).hexdigest()
        content_type = 'application/json'
        date_string = time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.gmtime())
        nonce = int(round(time.time() * 1000))

        signature = self.__sign("POST",
                                resource_uri,
                                content_md5,
                                content_type,
                                date_string,
                                nonce)
        auth_header = '%s key="%s", nonce="%s", signature="%s"' % (M800Api.AUTHENTICATION_SCHEME, self.key, nonce, signature)

        headers = {}
        headers['Content-Type'] = content_type
        headers[M800Api.EXPLICIT_DATE] = date_string
        headers[M800Api.CONTENT_MD5_HEADER] = content_md5
        headers['Authorization'] = auth_header

        url = urlparse.urlunparse((self.scheme,
                                   self.host + ":" + str(self.port),
                                   resource_uri,
                                   '',
                                   '',
                                   ''))
        request = urllib2.Request(url, payload, headers)
        response = urllib2.urlopen(request)
        return response.read()

    def __sign(self, method, request_uri, content_md5, content_type, date_string, nonce):
        _md5 = "" if content_md5 is None else content_md5
        _type = "" if content_type is None else content_type
        _payload = "%s\n%s\n%s\n%s\n%s\n%s" % (method, request_uri, _md5, _type, date_string, nonce)
        return hmac.new(self.secret, msg=_payload, digestmod=hashlib.sha256).hexdigest()