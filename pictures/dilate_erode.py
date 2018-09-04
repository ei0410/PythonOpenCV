import cv2
import numpy as np

def main():
    img = cv2.imread("purin.jpeg")

    times = 1000
    kernel = np.ones((3, 3), np.uint8)

    for i in range(times):
        img = cv2.erode(img, kernel)
        img = cv2.dilate(img, kernel)

    cv2.imshow("raw.jpeg", img)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
