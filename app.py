import cv2
from PIL import Image, ImageGrab
import numpy as np
import pyautogui
import time

template =  cv2.imread('love.png',0)
w, h = template.shape[::-1]

while True:
	im2 = ImageGrab.grab(bbox =(0, 0, 1920, 900))
	    
	im2.save('im.png')
	screen = cv2.imread('im.png',0)
	res = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
	threshold = 0.8
	loc = np.where( res >= threshold)
	for pt in zip(*loc[::-1]):
		cv2.rectangle(screen, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
		# print(pt[0],pt[1],pt[0] + w, pt[1] + h)
		x = int((pt[0]+pt[0]+w)/2)
		y = int((pt[1]+pt[1]+w)/2)
		# print(x,y)
	bbox = cv2.imwrite('res.png',screen)
	scr_show = cv2.resize(screen,(1024,576) )
	cv2.imshow('screen',scr_show)

	pyautogui.click(x,y)
	time.sleep(1)
	print(x,y)

		# pyautogui.click(x,y)
		# time.sleep(2)
	k=cv2.waitKey(20) & 0xff
	if k==27:
		break
print('Exiting...')
cv2.destroyAllWindows()