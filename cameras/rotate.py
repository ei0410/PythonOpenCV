import cv2
import numpy as np

def main():
    cap = cv2.VideoCapture(0)

    theta = 0
    
    while(cap.isOpened()):
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        scale = 1.0

        oy, ox = int(gray.shape[0]/2), int(gray.shape[1]/2)

        R = cv2.getRotationMatrix2D((ox, oy), theta, scale)
        dst = cv2.warpAffine(gray, R, gray.shape, flags=cv2.INTER_CUBIC)

        cv2.imshow("raw", dst)

        theta = theta + 1
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()
