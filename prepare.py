#!/usr/bin/env python
# -*- coding: utf-8 -*-

from proteus import ProteusClient
from ConfigParser import SafeConfigParser
import os

def get_client():
    print "Logging in..."
    ini = SafeConfigParser()
    ini.read(os.path.expanduser('~/.proteus'))
    API_USER = ini.get('account','username')
    API_PASSWD = ini.get('account','password')
    SERVER_URL = ini.get('account','server')
    DEVSERVER_URL = ini.get('account','devserver')
    CONFIG_NAME = ini.get('account','default_config_name')
    client = ProteusClient(SERVER_URL, API_USER, API_PASSWD, CONFIG_NAME)

    client.login()

    return client


    # client.logout()
    # exit(0)