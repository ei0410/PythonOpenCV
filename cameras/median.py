import cv2
import numpy as np

def main():
    cap = cv2.VideoCapture(0)
    
    val = 3

    median = 20

    flag = True

    while(cap.isOpened()):
        ret, frame = cap.read()

        if flag == True:
            val = val + 2
            if val > median:
                flag = False

        if flag == False:
            val = val - 2
            if val < 3:
                flag = True

        frame = cv2.medianBlur(frame, val)

        cv2.imshow("raw", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()
