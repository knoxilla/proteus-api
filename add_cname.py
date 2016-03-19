#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from pprint import pprint as pp

from prepare import get_client as Client

import logging

client = None

def main(argv):
    if(len(sys.argv) != 3):
        sys.exit('Usage: %s <FQDN-of-CNAME> <FQDN-of-target>' % (sys.argv[0]))
    aliashost = argv[1]
    targethost = argv[2]

    logging.basicConfig(level=logging.INFO)
    #logging.getLogger('suds.client').setLevel(logging.DEBUG)

    global client
    client = Client()

    hostname = aliashost.split(".")[0]
    zonename = 'engin.umich.edu' # just the rest of aliashost

    # already exists?
    print "Checking if exists...\n"
    if already_exists(hostname, zonename):
        exit(0)

# update code play
        # print check.properties._property_string
        # # going for raw Suds approach with replacement object for update()
        # newent = client._client.factory.create("APIEntity")
        # newent.name = check.name
        # newent.id = check.id
        # newent.type = check.type
        # # change a property on original
        # check.properties.ttl = 240L
        # check.properties.linkedRecordName = "www-wp.engin.umich.edu"
        # # generate the prop string we need for suds/proteus
        # plist = check.properties._property_list
        # prop_string = "|".join(['%s=%s' % (p, getattr(check.properties,p)) for p in plist])
        # # set it on the new replacement entity
        # print prop_string
        # newent.properties = prop_string
        # # try to update!
        # try:
        #     client.get_dns().update(entity=newent)
        #     print "didit"
        # except suds.WebFault as detail:
        #     print detail
        # exit(0)

    # add CNAME pointing to targethost
    print "Adding it...\n"
    client.get_dns().add_cname_record(aliashost, targethost, 600L, "",view_name="Default View")

    # re-check it
    print "Double-checking it...\n"
    recheck=client.get_dns().get_cname_record(hostname, zonename, view_name='Default View')

    print recheck.name
    print recheck.type
    print recheck.id
    pp(recheck.properties)

    client.logout()

    exit(0)

def already_exists(hostname, zonename):
    check = client.get_dns().get_cname_record(hostname, zonename, view_name='Default View')

    if check:
        print "CNAME %s.%s already exists. Update instaead? :)\n" % (hostname, zonename)
        return True
    else:
        return False

if __name__ == '__main__':
    main(sys.argv)
