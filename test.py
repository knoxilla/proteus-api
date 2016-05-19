#!/usr/bin/env python
# -*- coding: utf-8 -*-

from proteus import ProteusClient
import sys
import os
from pprint import pprint as pp
from ConfigParser import SafeConfigParser

import logging

def main(argv):

    logging.basicConfig(level=logging.INFO)
    #logging.getLogger('suds.client').setLevel(logging.DEBUG)

    # Parse config
    ini = SafeConfigParser()
    ini.read(os.path.expanduser('~/.proteus'))
    API_USER = ini.get('account','username')
    API_PASSWD = ini.get('account','password')
    PRODSERVER_URL = ini.get('account','server')
    DEVSERVER_URL = ini.get('account','devserver')
    CONFIG_NAME = ini.get('account','default_config_name')

    # Choose a server
    #SERVER_URL = PRODSERVER_URL
    SERVER_URL = DEVSERVER_URL

    print "Logging in to %s..." % (SERVER_URL)
    client = ProteusClient(SERVER_URL, API_USER, API_PASSWD, CONFIG_NAME)
    client.login()

    print "\nGet MX record..."
    mx_test = client.get_dns().get_mx_record('www','engin.umich.edu',view_name='Default View')

    if mx_test:
        print mx_test
        pp(mx_test)

    print "\nGet CNAME record..."
    cname_test = client.get_dns().get_cname_record('developer','engin.umich.edu',view_name='Default View')

    if cname_test:
        print cname_test
        print cname_test.id
        print cname_test.name
        print cname_test.type
        pp(cname_test.properties)
        print cname_test.properties.absoluteName
        print cname_test.properties.linkedRecordName

    #print client.get_dns().get_view("Default View")
    #print client.get_dns().get_view("Default View").id

    print "\nGet External Host record..."
    exthost_test = client.get_dns().get_externalhost_record("ec2-54-210-113-20.compute-1.amazonaws.com","nope",view_name="Default View")

    if exthost_test:
        print exthost_test
        print exthost_test.id
        print exthost_test.name
        print exthost_test.type
        pp(exthost_test.properties)

    print "\nLogging out..."
    client.logout()

    exit(0)

if __name__ == '__main__':
    main(sys.argv)


