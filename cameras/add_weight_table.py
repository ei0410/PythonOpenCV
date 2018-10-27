import cv2
import math
import numpy as np

def main():
    cap = cv2.VideoCapture(0)

    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

    weight = create_cos(height, width)
    
    while(cap.isOpened()):
        ret, frame = cap.read()

        #result = cv2.multiply(frame, weight)

        cv2.imshow("raw", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def create_cos(rows, cols):
    weight = np.zeros((rows, cols, 3), np.float32)
    center = (rows/2, cols/2)
    radius = math.sqrt(center[0]**2 + center[1]**2)

    for r in range(rows):
        for c in range(cols):
            distance = math.sqrt((center[0] - r)**2 + (center[1] - c)**2)

            radian = (distance / radius) * math.pi

            Y = (math.cos(radian) + 1.0) / 2.0
            weight[r, c] = [Y, Y, Y]

    return weight

if __name__=='__main__':
    main()
