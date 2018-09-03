import cv2
import numpy as np

def main():
    img = cv2.imread("purin.jpeg")

    if img is None:
        print("The file is nothing.")
        import sys
        sys.exit()

    rgb = cv2.split(img)
    blue  = rgb[0]
    green = rgb[1]
    red   = rgb[2]

    cv2.imshow("blue.jpeg" , blue)
    cv2.imshow("green.jpeg", green)
    cv2.imshow("red.jpeg"  , red)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
