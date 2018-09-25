# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 18:37:12 2018

@author: xiaojing
"""

from __future__ import print_function
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
import os
import sys


url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" +sys.argv[1] +"&VehicleMonitoringDetailLevel=calls&LineRef=" + sys.argv[2] 
response = urllib.urlopen(url)

data = response.read().decode("utf-8")

#use the json.loads method to obtain a dictionary representation of the responose string 

dataDict = json.loads(data)

records = dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

#record 元素1 在records理
#for record in records:
#    print(record['MonitoredVehicleJourney']['VehicleLocation'])
    
print("Bus line : " + sys.argv[2])
#test 
#print (len(records))
print("Number of Active Buses : " + str(len(records)))

for i in range(0,len(records)):
    print("Bus %s is at latitude %s and longitude %s"%(i,records[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude'],records[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']))
    