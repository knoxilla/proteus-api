#!/usr/bin/env python

# https://proteus1.umnet.umich.edu/Services/API?wsdl

from proteus import ProteusClient as pclient
import sys
import os
from pprint import pprint as pp
from ConfigParser import SafeConfigParser

def main(argv):
    if(len(sys.argv) != 3):
        sys.exit('Usage: %s <FQDN-of-CNAME> <FQDN-of-target>' % (sys.argv[0]))
    aliashost = argv[1]
    targethost = argv[2]

    # read ini file
    ini = SafeConfigParser()
    ini.read(os.path.expanduser('~/.proteus'))   
    # config
    API_USER = ini.get('account','username')
    API_PASSWD = ini.get('account','password')
    SERVER_URL = ini.get('account','server')
    DEVSERVER_URL = ini.get('account','devserver')
    CONFIG_NAME = ini.get('account','default_config_name')
    # get client and login
    a = pclient(SERVER_URL, API_USER, API_PASSWD, CONFIG_NAME)
    a.login()

    zonename = 'engin.umich.edu'
    hostname = aliashost.split(".")[0]

    # already exists?
    x=None
    x=a.get_dns().get_cname_record(hostname, zonename, view_name='Default View')
    if x:
        print "\n%s already exists as a CNAME record.  :)\n" % (aliashost)
        exit(0)

    # add CNAME pointing to targethost
    a.get_dns().add_cname_record(aliashost, targethost, 600L, "",view_name="Default View")

    # check it
    b=a.get_dns().get_cname_record(hostname, zonename, view_name='Default View')

    print b.name
    print b.type
    print b.id

    pp(b.properties)

    a.logout()

    exit(0)

if __name__ == '__main__':
    main(sys.argv)
