import cv2
import numpy as np

def main():
    img = cv2.imread("purin.jpeg")

    if img is None:
        print("The file is nothing.")
        import sys
        sys.exit()

    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    cv2.imshow("binary.jpeg", binary)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
