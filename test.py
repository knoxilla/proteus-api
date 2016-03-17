#!/usr/bin/env python

# the WSDL
# https://proteus1.umnet.umich.edu/Services/API?wsdl

from proteus import ProteusClient as pclient
import sys
import os
from pprint import pprint as pp
from ConfigParser import SafeConfigParser

if __name__=='__main__':
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
    #b=a.get_txt_record('_kerberos.opsec-auth-test1.ops.expertcity.com',view_name='Internal')
    #b=a.get_hinfo_record('dc2-dc2db','ops.expertcity.com',view_name='Internal')
    #b=a.get_cname_record('booterlin1','ops.expertcity.com',view_name='Internal')
    b=a.get_dns().get_mx_record('api','engin.umich.edu',view_name='Default View')
    b=a.get_dns().get_cname_record('developer','engin.umich.edu',view_name='Default View')
    #print b
    #pp(b)
    print b.id
    print b.name
    print b.type
    #print b.properties
    #pp(b.properties)
    print b.properties.absoluteName
    print b.properties.linkedRecordName

    print a.get_dns().get_view("Default View")
    print a.get_dns().get_view("Default View").id

    #a.get_dns().add_cname_record("archiva.engin.umich.edu","ec2-54-208-12-95.compute-1.amazonaws.com", 300L, "", view_name="Default View")
     
    #a.get_dns().add_cname_record("la-dee-dah.engin.umich.edu","engin-vhost.engin.umich.edu", 600L, "",view_name="Default View")

    b=a.get_dns().get_externalhost_record("ec2-54-210-113-20.compute-1.amazonaws.com","nope",view_name="Default View")

    print b
    print b.name
    print b.type
    print b.id

    # add externalhost
##    targethost = "openshift-master.caen-aws.engin.umich.edu"
    #a.get_dns().add_externalhost_record(targethost,"",view_name="Default View")

    # add CNAME pointing to externalhost
##    aliashost =  "far.engin.umich.edu"
    #a.get_dns().add_cname_record(aliashost, targethost, 600L, "",view_name="Default View")
 
    #print b.properties.addresses
    #print b.properties.reverseRecord
    #c=a.get_hinfo_record('_kerberos.opsec-auth-test1','ops.expertcity.com',view_name='Internal')
    #print c
    #d=a.get_dns().get_zone_list('engin.umich.edu',view_name='Default view')
    #for i in d:
    #    print '%s - %s' % (i.name,i.type)
    a.logout()
