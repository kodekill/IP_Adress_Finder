#!/bin/sh

sleep 15
cd /

cd home/pi/Public/IP_Address_Finder

/sbin/ifconfig | grep -A 3 wlan0 | grep -m 1 inet > addr.txt
sudo python address.py

cd /
