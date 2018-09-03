import cv2
import numpy as np

def main():
    img = cv2.imread("purin.jpeg", cv2.IMREAD_GRAYSCALE)

    if img is None:
        print("The file is nothing.")
        import sys
        sys.exit()

    equal = cv2.equalizeHist(img)
    cv2.imshow("equal.jpeg", equal)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
