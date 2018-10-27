import cv2
import numpy as np

def main():
    MAX_CORNERS = 50
    BLOCK_SIZE = 3
    QUALITY_LEVEL = 0.01
    MIN_DISTANCE = 20.0

    img = cv2.imread("purin.jpeg")

    if img is None:
        print("The file is nothing.")
        import sys
        sys.exit()

    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    corners = cv2.goodFeaturesToTrack(gray, MAX_CORNERS, QUALITY_LEVEL, MIN_DISTANCE, blockSize = BLOCK_SIZE, useHarrisDetector = False)

    for i in corners:
        x, y = i.ravel()
        cv2.circle(img, (x,y), 4, (255, 255, 0), 2)

    cv2.imshow("gray.jpeg", img)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
