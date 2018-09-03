import cv2
import numpy as np

def main():
    img = cv2.imread("purin.jpeg", cv2.IMREAD_GRAYSCALE)

    if img is None:
        print("The file is nothing.")
        import sys
        sys.exit()

    binary = cv2.adaptiveThreshold(img, 200, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 7, 8)
    cv2.imshow("binary.jpeg", binary)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
