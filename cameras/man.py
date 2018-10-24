import cv2
import numpy as np
import datetime

def main():
    # get camera
    cap = cv2.VideoCapture(0)

    # set cascade file
    cascade = cv2.CascadeClassifier("haarcascade_fullbody.xml")

    save_path = "./outputs/"

    count = 0
    
    while(cap.isOpened()):
        # get camera image
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        man = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(30, 30))

        now = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")

        #for (x, y, w, h) in man:
        #    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 200), 3)

        if len(man) > 0:
            cv2.imwrite(save_path + now + ".jpg", frame)
            print now
            count += 1
            #if count > 5:
            #    break

        cv2.imshow("image", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()
