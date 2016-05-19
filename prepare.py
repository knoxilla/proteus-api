#!/usr/bin/env python
# -*- coding: utf-8 -*-

from proteus import ProteusClient
from ConfigParser import SafeConfigParser
import os

def get_client():
    # Parse config...
    ini = SafeConfigParser()
    ini.read(os.path.expanduser('~/.proteus'))
    API_USER = ini.get('account','username')
    API_PASSWD = ini.get('account','password')
    PRODSERVER_URL = ini.get('account','server')
    DEVSERVER_URL = ini.get('account','devserver')
    CONFIG_NAME = ini.get('account','default_config_name')

    # Choose a server
    SERVER_URL = PRODSERVER_URL
    #SERVER_URL = DEVSERVER_URL

    print "Logging in to %s...\n" % (SERVER_URL)
    client = ProteusClient(SERVER_URL, API_USER, API_PASSWD, CONFIG_NAME)
    client.login()
    return client
