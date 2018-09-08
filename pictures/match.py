import cv2
import numpy as np

def main():
    cards = cv2.imread("cards.png")
    temp  = cv2.imread("temp.png")
    
    if cards is None or temp is None:
        print("No pngfile")
        import sys
        sys.exit()

    result = cv2.matchTemplate(cards, temp, cv2.TM_CCOEFF_NORMED)
    mmr = cv2.minMaxLoc(result)
    pos = mmr[3]

    dst = cards.copy()
    cv2.rectangle(dst, pos, (pos[0] + temp.shape[1], pos[1] + temp.shape[0]), (0, 0, 255), 2)

    cv2.imshow("result", dst)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
