import cv2
import numpy as np

def main():
    cap = cv2.VideoCapture(0)

    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

    img = cv2.imread("raspi.jpg")

    if img is None:
        print("No image")
        import sys
        sys.exit()

    img = cv2.resize(img, (width, height))

    while(cap.isOpened()):
        ret, frame = cap.read()

        result = cv2.bitwise_or(frame, img)

        cv2.imshow("raw", result)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()
