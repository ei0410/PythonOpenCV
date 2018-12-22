#!/usr/bin/env python

import cv2

def main():
	img = cv2.imread("input.jpg")

	cascade = cv2.CascadeClassifier("lbpcascade_animeface.xml")

	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	face = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(30, 30))

	for (x, y, w, h) in face:
		cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 200), 3)
	
	#cv2.imwrite("output.jpg", img)
	cv2.imshow("output.jpg", img)
	cv2.waitKey(0)

if __name__ == '__main__':
	main()
