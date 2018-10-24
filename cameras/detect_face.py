import cv2
import numpy as np
import sys

def main():
    argvs = sys.argv
    argc  = len(argvs)

    if argc != 2:
        print "Usage: #python %s filename" % argvs[0]
        sys.exit()

    read_path = "./outputs/"

    image = cv2.imread(read_path + argvs[1])

    if len(image.shape) == 3:
        height, width, channel = image.shape[:3]

    cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    save_path = "./outputs/"

    if image is None:
        print("The file is nothing.")
        sys.exit()

    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    face = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(30, 30))

    #x = face[0][0]
    y = face[0][1]
    #w = face[0][2]
    h = face[0][3]

    dst = image[y+h:height, 0:width]

    if len(face) > 0:
        cv2.imwrite(save_path + "result.jpg", dst)

    cv2.imshow("result.jpg", dst)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
