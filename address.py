import time
import re
from time import sleep

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def check():
	previous_line = ""
	with open('addr.txt','r') as infile: 
    		for current_line in infile: 
        		if 'wlan0' in previous_line: 
            			return current_line 
        		previous_line = current_line

def reg():
	temp = check()
	ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}',temp)
	return ip

try:   		
	if __name__ == '__main__':
               
        	ip_address = check()
	        text1 = ip_address[20:35]
	
		#ip_address = reg()
		#text1 = ip_address[1:2]
	
		# Raspberry Pi pin configuration:
	        RST = 24

	        # 128x64 display with hardware I2C:
	        disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

        	width = disp.width
	        height = disp.height
	        image = Image.new('1', (width, height))
	        draw = ImageDraw.Draw(image)

	        # Draw some shapes.
	        # First define some constants to allow easy resizing of shapes.
	        padding = 0
	        shape_width = 0
	        top = padding
	        bottom = height-padding
	        # Move left to right keeping track of the current x position for drawing shapes.
	        x = padding
	        font = ImageFont.load_default()

	        # Initialize library.
        	disp.begin()

	        # Clear display.
	        disp.clear()
	        disp.display()

	        # Write two lines of text.
	        draw.text((x, top), 'IP Address is:',  font=font, fill=255)
        	draw.text((x, top+20), text1, font=font, fill=255)

	        # Display image.
        	disp.image(image)
	        disp.display()
		
		draw.text((x+60, top+50), 'Erase in:', font= font, fill=255)
		disp.image(image)
		disp.display()
			
		timmer_count = 20
		while (timmer_count > 0):
			draw.text((x+115, top+50), str(timmer_count), font=font, fill=255)
			disp.image(image)
			disp.display()
			time.sleep(1)
			timmer_count -= 1
				
			draw.rectangle((x+110, top+45, width, height), outline=0, fill=0)
			disp.image(image)
			disp.display()
				
		disp.clear()
		disp.display()

except KeyboardInterrupt:
	print "Program Terminated \n"

except:
	print "Other Error Occured"

finally:
	disp.clear()
	disp.display()
