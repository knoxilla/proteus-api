#!/usr/bin/env python

# the WSDL
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
    pp(aliashost)

    targethost = argv[2]
    pp(targethost)

    # read ini file
    ini = SafeConfigParser()
    ini.read(os.path.expanduser('~/.proteus'))   
    ## Set values for later use - configure here if you must
    API_USER = ini.get('account','username')
    API_PASSWD = ini.get('account','password')
    SERVER_URL = ini.get('account','server')
    DEVSERVER_URL = ini.get('account','devserver')
    CONFIG_NAME = ini.get('account','default_config_name')
    a = pclient(SERVER_URL, API_USER, API_PASSWD, CONFIG_NAME)
    a.login()

    print a.get_dns().get_view("Default View")
    print a.get_dns().get_view("Default View").id
    
    # add CNAME pointing to targethost
    a.get_dns().add_cname_record(aliashost, targethost, 600L, "",view_name="Default View")

    zone = 'engin.umich.edu'
    hostname = ''
    b=a.get_dns().get_cname_record(zone, hostname, view_name='Default View')

    print b.id
    print b.name
    print b.type
    pp(b.properties)
    #print b.properties.absoluteName
    #print b.properties.linkedRecordName 

    a.logout()

    exit(0)

if __name__ == '__main__':
    main(sys.argv)
