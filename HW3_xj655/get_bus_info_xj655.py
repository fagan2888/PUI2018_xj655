#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 21:56:36 2018

@author: xiaojing
"""

# -*- coding: utf-8 -*-
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
##use the json.loads method to obtain a dictionary representation of the responose string 
dataDict = json.loads(data)
##print(data)

fout = open(sys.argv[3],'w')
fout.write("Longitude,Latitude,Stop name, Stop status\n")
records = dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
for i in range(0,len(records)):
    record_longitude = records[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    record_latitude = records[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    
    try:
        record_stopname = records[i]['MonitoredVehicleJourney']['MonitoredCall']["StopPointName"]
    except LookupError:
        record_stopname = 'N/A'
        
    try:
        record_stop_status = records[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]["Extensions"]["Distances"]["PresentableDistance"]
    except LookupError:
        record_stop_status = 'N/A'
    print(record_longitude,record_latitude,record_stopname, record_stop_status)
    fout.write('%s,%s,%s,%s\n'%(record_longitude,record_latitude,record_stopname,record_stop_status))
    
fout.close()

###record 元素1 在records里面
##for record in records:
##    print(record['MonitoredVehicleJourney']['VehicleLocation'])
##test 
##print (len(records))

    
#print("Bus line : " + sys.argv[2])
#print("Number of Active Buses : " + str(len(records)))
#for i in range(0,len(records)):
#    print("Bus %s is at latitude %s and longitude %s"%(i,records[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude'],records[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']))
    