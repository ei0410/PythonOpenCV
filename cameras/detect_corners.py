import cv2
import numpy as np

def main():
    MAX_CORNERS = 50
    BLOCK_SIZE = 3
    QUALITY_LEVEL = 0.01
    MIN_DISTANCE = 20.0

    cap = cv2.VideoCapture(0)
    
    while(cap.isOpened()):
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

        corners = cv2.goodFeaturesToTrack(gray, MAX_CORNERS, QUALITY_LEVEL, MIN_DISTANCE, blockSize = BLOCK_SIZE, useHarrisDetector = False)

        for i in corners:
            x, y = i.ravel()
            cv2.circle(frame, (x, y), 4, (255, 255, 0), 2)

        cv2.imshow("raw", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()
