import cv2
import numpy as np

def main():
    img = cv2.imread("purin.jpeg")

    if img is None:
        print("The file is nothing.")
        import sys
        sys.exit()

    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    cv2.imshow("gray.jpeg", gray)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
