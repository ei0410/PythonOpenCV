import cv2
import numpy as np

def main():

    SCALE = 1

    for i in range(10):
        img = cv2.imread("yajyu.jpg")
        height = img.shape[0]
        width  = img.shape[1]

        img = cv2.resize(img, (int(width*SCALE), int(height*SCALE)), interpolation = cv2.INTER_NEAREST)
        img = cv2.resize(img, (width, height), interpolation = cv2.INTER_NEAREST)

        cv2.imshow("mozaic", img)
        
        SCALE = SCALE * 0.6

        cv2.waitKey(0)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
