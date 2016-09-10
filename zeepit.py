#!/usr/bin/env python
# -*- coding: utf-8 -*-

import zeep

wsdl = 'http://www.soapclient.com/xml/soapresponder.wsdl'
client = zeep.Client(wsdl=wsdl)
print(client.service.Method1('Zeep', 'is cool'))

#wsdl2 = 'https://proteus1.umnet.umich.edu/Services/API?wsdl'
#client2 = zeep.Client(wsdl=wsdl2)
#print(client2.service.Method1())
