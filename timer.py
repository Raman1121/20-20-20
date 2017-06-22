import subprocess as s
import time

def countdown(n):
	while n >0:
		n=n-1
		time.sleep(1)
		if n==0:
			s.call(['notify-send', '20-20-20', 'Woah man! Take a rest for 20 sec!!'])

countdown(1200)



