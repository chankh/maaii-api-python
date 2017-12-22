Python REST API for M800 online platform.
=========================================

This API allows Python developers to easily connect to M800's online
platform. It handles all of the low-level tasks such as generating and
signing requests, connecting to the server, and parsing server
responses.

Requirements
------------
* Python 2.7+

Usage
-----
For basic calls to M800's online platform, you should add the following
line to your Python code:

```
from M800Api import M800Api
```

In order to use the API, you need to construct an instance of the
M800Api class. This class contains the parameters used to connect to
the server.

```
api = M800Api( "key", "secret", host", port );
```

Where host is the hostname or IP address of M800's online platform API
server (i.e. api.m800.com), port is the IP port number used to connect
to the server (generally 80 for HTTP and 443 for HTTPS), key is the
developer's unique key, and the secret is the shared secret matching to
the developer key that you are using.

After you have created your M800Api object, you can use the methods on
the object to communicate with M800's online platform. For instance, to
send a text SMS message:

```
response = api.send_text_sms("<sender's number>",
                             "<recipient's number>",
                             "normal",
                             "text SMS through M800");
```

The send_text_sms method will return a JSON object which you can use to
inspect the results returned from the server.

Running the Sample
------------------

The sample code to send a text SMS is written in the M800ApiTest.py file.

Edit the contents in M800ApiTest.py with your developer key, secret,
sender and receiver phone numbers. Then, execute from the command line
using:

```
python M800ApiTest.py
```

License
-------

M800 SMS-API Sample Code
Copyright 2014 M800 www.m800.com


THIS M800 SOFTWARE IS PROVIDED BY M800 ON AN "AS IS" BASIS AND WITHOUT
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, WITHOUT LIMITATION, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND`# FITNESS FOR A PARTICULAR
PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL M800 BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, IN ANY CIRCUMSTANCES, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR ITS USE.

For more infomration, please visit <http://www.m800.com> (General T&C)
