import cv2
import numpy as np

def main():
    cap = cv2.VideoCapture(0)
    
    val = 1

    limit = 55

    flag = True

    deflag = True

    while(cap.isOpened()):
        ret, frame = cap.read()

        kernel = np.ones((val, val), np.uint8)

        val = val + 2

        if deflag == True:
            if flag == True:
                frame = cv2.dilate(frame, kernel)
                #frame = cv2.erode(frame, kernel)
                flag = False

            if flag == False:
                frame = cv2.erode(frame, kernel)
                #frame = cv2.dilate(frame, kernel)
                flag = True

        if val > limit:
            val = limit
            deflag = False
            cv2.waitKey(0)
            break

        cv2.imshow("raw", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()
