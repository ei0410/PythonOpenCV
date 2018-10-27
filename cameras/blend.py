import cv2
import numpy as np

def main():
    cap = cv2.VideoCapture(0)

    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

    img = cv2.imread("purin.jpeg")

    if img is None:
        print("No image")
        import sys
        sys.exit()

    img = cv2.resize(img, (width, height))

    rate = 0.0
    
    while(cap.isOpened()):
        ret, frame = cap.read()

        result = cv2.addWeighted(frame, 1 - rate,  img, rate, 0.0)
        cv2.imshow("raw", result)

        rate  = rate + 0.01
        if rate >= 1.0:
            rate = 0.0
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()
