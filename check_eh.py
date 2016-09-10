#!/usr/bin/env python
# -*- coding: utf-8 -*-

# what cnames point at a given EH (by entityId):
# client._client.service.getLinkedEntities(15855813,"AliasRecord",0,10)

import sys
import os
from pprint import pprint as pp

from prepare import get_client as Client

import logging

client = None

def main(argv):
    if(len(sys.argv) != 2):
        sys.exit('Usage: %s <FQDN-of-ExternalHost>' % (sys.argv[0]))
    targethost = argv[1]

    logging.basicConfig(level=logging.INFO)
    #logging.getLogger('suds.client').setLevel(logging.DEBUG)

    global client
    client = Client()

    # already exists?
    print "Checking if exists...\n"
    if already_exists(targethost):
        exit(1)

    # stop here - exit cleanly if it does NOT exist
    exit(0)

    # add externalhost
    client.get_dns().add_externalhost_record(targethost,'',view_name="Default View")

    # re-check it
    recheck=client.get_dns().get_externalhost_record(targethost,"nope",view_name="Default View")

    # double-check results
    print recheck.name
    print recheck.type
    print recheck.id
    pp(recheck.properties)

    client.logout()

    exit(0)

def already_exists(targethost):
    check = client.get_dns().get_externalhost_record(targethost,"nope",view_name="Default View")
    if check:
        print "ExternalHost %s already exists.\n" % (targethost)
        print check.id
        print check.name
        pp(check.properties)
        pp(client._client.service.getLinkedEntities(check.id,"AliasRecord",0,10))
        return True
    else:
        return False

if __name__ == '__main__':
    main(sys.argv)
