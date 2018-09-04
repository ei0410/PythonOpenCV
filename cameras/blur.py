import cv2
import numpy as np

def main():
    cap = cv2.VideoCapture(0)
    
    val = 0

    blur_size = 20

    flag = True

    while(cap.isOpened()):
        ret, frame = cap.read()

        if flag == True:
            val = val + 1
            if val > blur_size:
                flag = False

        if flag == False:
            val = val - 1
            if val == 1:
                flag = True

        frame = cv2.blur(frame, (val, val))

        cv2.imshow("raw", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()
