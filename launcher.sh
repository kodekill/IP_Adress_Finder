#!/bin/sh

sleep 15 
cd /


cd home/pi/Address
/sbin/ifconfig > addr.txt
sudo python address.py
cd /
