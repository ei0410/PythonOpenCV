import cv2
import numpy as np

def main():
    cap = cv2.VideoCapture(0)
    
    while(cap.isOpened()):
        ret, frame = cap.read()
        cv2.imshow("raw", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()
