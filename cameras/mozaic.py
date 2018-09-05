import cv2
import numpy as np

def main():
    cap = cv2.VideoCapture(0)

    SCALE = 1
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

    while(cap.isOpened()):
        ret, frame = cap.read()

        frame = cv2.resize(frame, (int(width*SCALE), int(height*SCALE)))
        frame = cv2.resize(frame, (width, height))

        cv2.imshow("raw", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()
