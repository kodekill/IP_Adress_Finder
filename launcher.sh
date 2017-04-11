#!/bin/sh
#launcher.sh
sleep 15 
cd /


cd home/pi/Address
/sbin/ifconfig > addr.txt
sudo python address.py
cd /



#These lines will turn the camera on and start recording on boot
#cd home/pi/LOAVES
#sudo python Camera_Project.py
cd /
