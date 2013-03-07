To run:

1. Install [Python ZSI][1]
2. Turn the [WSDL][2] file into code - `wsdl2py -b phonero_remix.wsdl`
3. Edit and Run the script - `./sms.py`


This client is meant as an example of how to communicate with an [Outlook OMS SMS Gateway][3] using Python and ZSI. There are a number of services on the Internet that allow you to send SMS from Outlook via the Outlook OMS protocol. My service provider had one such gateway, but the documentation only described the outer wrapper of the message.

* [The Microsoft Full WSDL][4]
* [Phonero OMSService address][5]

The big issue was the xmsData portion of the message. Further complicating matters was the use of SSL in the official client so that I couldn't see a sample message.

First, I got the official WSDL from Microsoft and tried mixing it with the Phonero WSDL so that I had a specification for xmsData portion. However, my constructed messages still failed as 400 Bad Request.

After a bit of time I began to look for ways to intercept the communication from the official client and peak inside. That is when I found [mitmproxy][6]. Mitmproxy is some of the coolest software ever.


Mitmproxy is a python application that acts as a man-in-the-middle generating certificates on the fly so you can intercept SSL communication. You just point Windows Internet Options at your mitmproxy instance and install the mitmproxy certificate authority. Really, really cool stuff. Do not assume that your protocol specification is protected by SSL.

Once I sent a message I could see that the xmsData was double wrapped. Dumb.

    <xmsData>
        <xmsData>
        </xmsData>
    </xmsData>

After clearing that up it just worked.

[1]: http://pywebsvcs.sourceforge.net
[2]: http://en.wikipedia.org/wiki/Web_Services_Description_Language
[3]: http://msdn.microsoft.com/en-us/library/ff606754.aspx
[4]: http://msdn.microsoft.com/en-us/library/dd965730(v=office.12).aspx
[5]: https://services.gomobile.no/omsservice.asmx
[6]: http://mitmproxy.org
