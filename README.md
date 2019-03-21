# IP_Adress_Finder
Python code for an OLED I2C Screen


install these files: 
git clone https://github.com/adafruit/Adafruit_Python_GPIO.git
git clone https://github.com/adafruit/Adafruit_SSD1306


after install both:
cd Adafruit_Python_GPIO.git -> sudo python setup.py install
cd Adafruit_SSD1306 -> sudo pip install Adafruit-SSD1306


lastly:
cd IP_Address_Finder -> python address.py

run at boot:
sudo crontab -e

at bottom of file add:
@reboot /home/pi/Public/IP_Address_Finder/launcher.sh
