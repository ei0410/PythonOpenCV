import cv2
import numpy as np

def main():
    img1 = cv2.imread("gray_purin.jpeg", 0)
    img2 = cv2.imread("rotate_purin.jpeg", 0)

    if img1 is None or img2 is None:
        print("No files")
        import sys
        sys.exit()

    detector = cv2.ORB_create()
    keypoints1, descriptor1 = detector.detectAndCompute(img1, None)
    keypoints2, descriptor2 = detector.detectAndCompute(img2, None)

    out1 = cv2.drawKeypoints(img1, keypoints1, None)
    out2 = cv2.drawKeypoints(img2, keypoints2, None)

    matcher = cv2.BFMatcher(cv2.NORM_HAMMING)
    matches  = matcher.match(descriptor1, descriptor2)
    result = cv2.drawMatches(img1, keypoints1, img2, keypoints2, matches, None, flags=2)

    cv2.imshow("result", result)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
