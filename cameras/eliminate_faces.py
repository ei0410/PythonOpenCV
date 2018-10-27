import cv2
import numpy as np

def main():
    cap = cv2.VideoCapture(0)

    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

    cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    
    while(cap.isOpened()):
        ret, frame = cap.read()
        img = np.zeros((height, width, 3), np.uint8)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        face = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(30, 30))

        for (x, y, w, h) in face:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), -1)

        msk = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        frame = cv2.inpaint(frame, msk, 1, cv2.INPAINT_TELEA)

        cv2.imshow("raw", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()
