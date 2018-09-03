import cv2
import numpy as np

def main():
    img = cv2.imread("purin.jpeg")
    cv2.imshow("raw.jpeg", img)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
