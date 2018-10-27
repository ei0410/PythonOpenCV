import cv2
import numpy as np

def main():
    cap = cv2.VideoCapture(0)
    
    while(cap.isOpened()):
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        gray[gray<127]  = 0
        gray[gray>=127] = 255

        kernel = np.ones((6, 6), np.uint8)

        erode  = cv2.erode(gray, kernel)

        cv2.imshow("raw", erode)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()
