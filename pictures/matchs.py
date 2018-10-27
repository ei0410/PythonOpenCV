import cv2
import numpy as np

def main():
    cards = cv2.imread("cards.png", 0)
    cards_color = cv2.imread("cards.png")
    temp  = cv2.imread("mark.png", 0)
    
    if cards is None or cards_color is None or temp is None:
        print("No pngfile")
        import sys
        sys.exit()

    result = cv2.matchTemplate(cards, temp, cv2.TM_CCOEFF_NORMED)

    threshold = 0.9

    loc = np.where(result >= threshold)

    w, h = temp.shape[::-1]

    for top_left in zip(*loc[::-1]):
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(cards_color, top_left, bottom_right, (255, 0, 0), 2)

    cv2.imshow("result", cards_color)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
