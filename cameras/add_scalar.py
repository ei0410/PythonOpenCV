import cv2
import numpy as np

def main():
    cap = cv2.VideoCapture(0)

    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

    blue = np.zeros((height, width, 3), np.uint8)
    blue[:,:] = [128, 0, 0]

    while(cap.isOpened()):
        ret, frame = cap.read()

        result = cv2.add(frame, blue)
        cv2.imshow("raw", result)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()
