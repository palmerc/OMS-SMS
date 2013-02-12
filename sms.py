#!/usr/bin/python

import sys
import uuid
from OMSService_client import *

loc = OMSServiceLocator()
kw = { 'tracefile' : sys.stdout }
port = loc.getOMSServiceSoap(**kw)

deliverXmsMsg = DeliverXmsSoapIn()

xmsData = ns0.xmsData_Dec().pyclass()
xmsData.set_attribute_client('Python SMS Client 1.0')

user = xmsData.new_user()
user.UserId = ''
user.Password = ''
user.ReplyPhone = ''
user.CustomData = ''
xmsData.User = user

xmsHead = xmsData.new_xmsHead()
xmsHead.To = xmsHead.new_to()
xmsHead.To.Recipient = ['']
xmsHead.SourceType = 'other'
xmsHead.RequiredService = xmsHead.new_requiredService('SMS_SENDER')
xmsData.XmsHead = xmsHead

xmsBody = xmsData.new_xmsBody()
xmsBody.set_attribute_format('SMS')
content = xmsBody.new_content('Hello, World!')
content.set_attribute_contentType('text/plain')
content.set_attribute_contentId(str(uuid.uuid4()))
content.set_attribute_contentLocation('1.txt')
xmsBody.Content.append(content)
xmsData.XmsBody = xmsBody

writer = ZSI.SoapWriter(envelope=0)
deliverXmsMsg.XmsData = writer.serialize(xmsData)

rsp = port.DeliverXms(deliverXmsMsg)
