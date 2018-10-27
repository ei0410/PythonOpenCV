import cv2
import numpy as np

def main():
    cap = cv2.VideoCapture(0)
    
    while(cap.isOpened()):
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        canny = cv2.Canny(frame, 40.0, 200.0)
        #sobel = cv2.Sobel(frame, -1, 0, 1)

        cv2.imshow("raw", canny)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()
