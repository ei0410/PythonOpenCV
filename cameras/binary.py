import cv2
import numpy as np

def main():
    cap = cv2.VideoCapture(0)
    
    while(cap.isOpened()):
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        ret, th = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

        #th = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

        #ret, th = cv2.threshold(gray, 0, 255, cv2.THRESH_OTHU)

        cv2.imshow("binary", th)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()
