import cv2
import numpy as np

def main():
    cap = cv2.VideoCapture(0)

    cascade = cv2.CascadeClassifier("haarcascade_eye.xml")
    
    while(cap.isOpened()):
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        face = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(30, 30))

        for (x, y, w, h) in face:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 200), 3)

        cv2.imshow("raw", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()
