#!/usr/env/bin python
# Documentation: http://www.pennington.net/py/ciscoconfparse/

from ciscoconfparse import CiscoConfParse
import re

ciscoConf = CiscoConfParse("ciscoConfig.cfg")

#Print crypto map CRYPTO and its offsprings
cryptoMap = ciscoConf.find_objects(r"^crypto map CRYPTO")

for item in cryptoMap: 
    print item.text
    for child in item.children:
        print child.text
        for grandchildren in child.children:
            print grandchildren.text

#Find all of the crypto map entries that are using PFS group2
print "*" * 10 + " With PFS Group 2"
for crypto  in cryptoMap:
    if crypto.has_child_with(r' set pfs group2'):
        print crypto.text
        print [item.text for item in crypto.children]
     

#Find the crypto maps that are not using AES (based-on the transform set name). Print these entries and their corresponding transform set name.
print "*" * 10 + " Not using AES"
for crypto in cryptoMap:
    if not crypto.has_child_with(r' set transform-set AES-SHA'):
        print crypto.text
        for line in crypto.children:
            if re.search("set transform-set", line.text):
                print line.text





