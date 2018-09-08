import cv2
import numpy as np

def main():
    img = cv2.imread("purin.jpeg", 0)

    theta = 30
    scale = 1.0

    oy, ox = int(img.shape[0]/2), int(img.shape[1]/2)

    R = cv2.getRotationMatrix2D((ox, oy), theta, scale)
    result = cv2.warpAffine(img, R, img.shape, flags=cv2.INTER_CUBIC)

    cv2.imwrite("rotate_purin.jpeg", result)
    cv2.imshow("raw.jpeg", result)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
