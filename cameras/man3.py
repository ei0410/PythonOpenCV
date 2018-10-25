import cv2
import numpy as np
import datetime

def main():
    # get camera
    cap = cv2.VideoCapture(0)

    save_path = 'outputs/'

    # Read cascade file
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    while(cap.isOpened()):
        # get camera image
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        hist_gray = cv2.equalizeHist(gray)
        faces = face_cascade.detectMultiScale(gray)

        # Create clf use Hog feature and SVM
        hog = cv2.HOGDescriptor()
        hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
        hogParam = {'winStride': (8, 8), 'padding': (32, 32), 'scale': 1.05}

        human, r = hog.detectMultiScale(gray, **hogParam)

        now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        for (mx, my, mw, mh) in human:
            cv2.rectangle(frame, (mx, my), (mx + mw, my + mh), (0, 0, 200), 3)
            for (fx, fy, fw, fh) in faces:
                cv2.rectangle(frame, (fx, fy), (fx+fw, fy+fh), (255, 0, 0), 2)

        if len(human) > 0 and len(faces) > 0:
            mx = human[0][0]
            my = human[0][1]
            mw = human[0][2]
            mh = human[0][3]

            fx = faces[0][0]
            fy = faces[0][1]
            fw = faces[0][2]
            fh = faces[0][3]

            dst = frame[my:my+mh, mx:mx+mw]

            if (mx < fx) and (my < fy) and (mx + mw > fx + fw) and (my + mh > fy + fh):
                dst = frame[my:my+mh, mx:mx+mw]
                #cv2.imwrite(save_path + now + ".jpg", frame)
                cv2.imwrite(save_path + now + ".jpg", dst)
                print('mx: '+str(mx)+'\t'+' my: '+str(my)+'\t'
                    +' mw: '+str(mw)+'\t'+' mh: '+str(mh)+'\t'
                    +' fx: '+str(fx)+'\t'+' fy: '+str(fy)+'\t'
                    +' fw: '+str(fw)+'\t'+' fh: '+str(fh))
            #cv2.imwrite(save_path + now + "_raw.jpg", frame)
            #cv2.imwrite(save_path + now + ".jpg", dst)
            #print(now)
            """
            print('mx: '+str(mx)+'\t'+' my: '+str(my)+'\t'
                +' mw: '+str(mw)+'\t'+' mh: '+str(mh)+'\t'
                +' fx: '+str(fx)+'\t'+' fy: '+str(fy)+'\t'
                +' fw: '+str(fw)+'\t'+' fh: '+str(fh))
            """

        cv2.imshow("image", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()
