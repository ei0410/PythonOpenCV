import cv2
img = cv2.imread("gazou.jpg")
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("gazou", img)
cv2.waitKey(0)
