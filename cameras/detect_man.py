import cv2

def main():
    cap = cv2.VideoCapture(0)
	#cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')
	f_cascade = cv2.CascadeClassifier('/home/ei0124/PythonOpenCV/cameras/haarcascade_fullbody.xml')
    while(cap.isOpened()):
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow("gray", gray)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()
