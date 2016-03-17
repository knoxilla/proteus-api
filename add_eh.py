#!/usr/bin/env python

# https://proteus1.umnet.umich.edu/Services/API?wsdl

from proteus import ProteusClient as pclient
import sys
import os
from pprint import pprint as pp
from ConfigParser import SafeConfigParser

def main(argv):

    if(len(sys.argv) != 2):
        sys.exit('Usage: %s <FQDN-of-ExternalHost>' % (sys.argv[0]))
    targethost = argv[1]

    # read ini file
    ini = SafeConfigParser()
    ini.read(os.path.expanduser('~/.proteus'))
    # config
    API_USER = ini.get('account','username')
    API_PASSWD = ini.get('account','password')
    SERVER_URL = ini.get('account','server')
    DEVSERVER_URL = ini.get('account','devserver')
    CONFIG_NAME = ini.get('account','default_config_name')
    # get client, login
    a = pclient(SERVER_URL, API_USER, API_PASSWD, CONFIG_NAME)
    a.login()

    # already exists?
    x=a.get_dns().get_externalhost_record(targethost,"nope",view_name="Default View")
    if x:
        print "\n%s already has an ExternalHost record.  :)\n" % (targethost)
        exit(0)

    # add externalhost
    a.get_dns().add_externalhost_record(targethost,'',view_name="Default View")

    # check it
    c=a.get_dns().get_externalhost_record(targethost,"nope",view_name="Default View")

    # double-check results
    print c.name
    print c.type
    print c.id

    a.logout()

    exit(0)

if __name__ == '__main__':
    main(sys.argv)
