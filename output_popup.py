#!/usr/bin/python2.7

import pprint
import pyeapi
import traceback
import subprocess
import re
import os
import mysql.connector

import ssl
import sys

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
#
i = sys.argv[1]
m = sys.argv[2]

splitIP = re.split('-', sys.argv[1])
#print splitIP[7]
IPlastoctet = int(splitIP[7]) + 100
IP = "10.129.32." + str(IPlastoctet)
#print IP


try:
    node = pyeapi.connect(transport="https", host=IP, username="xxx", password="xxxxx", port=None)
    config = "show running-config"
    run_config=node.execute([config])
    run_config_demet=run_config['result'][0]['cmds']['interface'+' '+m]['cmds']
    config_list=" "
    for  cmd in run_config_demet:
        config_list = config_list + '\n'+cmd+'<br>'
    print config_list

except Exception as e:
    print 'Error 2'
    print 'ERROR : >> ' + str(e)
    print(traceback.format_exc())
