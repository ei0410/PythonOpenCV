import cv2
import sys
import numpy as np

def main():
    cap = cv2.VideoCapture(0)

	hog = cv2.HOGDescriptor()
	hog.setSVMDetetor(cv2.HOGDescriptor_getDefaultPeopleDetector())
	hogParams = {'winStride': (8, 8), 'padding': (32, 32), 'scale':1.05}

    while(cap.isOpened()):
        ret, frame = cap.read()

		human, r = hog.detectMultScale(frame, **hogParams)

        for (x, y, w, h) in human:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 200), 3)

        cv2.imshow("image", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()
