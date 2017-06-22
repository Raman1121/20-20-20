import subprocess as s
import time
import os

def countdown(n):
	while n >0:
		n=n-1
		time.sleep(1)
		if n==0:
			img = os.path.abspath('20-20-20.jpg')
			
			s.Popen(['notify-send', '-i', img, '20-20-20', 'Woah man! Take a rest for 20 sec!!'])

countdown(1200)



