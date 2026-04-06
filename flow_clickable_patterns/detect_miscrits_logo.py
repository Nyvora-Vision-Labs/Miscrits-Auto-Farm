import cv2
from utils import screenshot

COORD1 = (3463, -539)
COORD2 = (3536, -467)
MONITOR_LEFT = 1920
MONITOR_TOP = -599

MISCRITS_DIR = "images/miscrits"
THRESHOLD = 0.5

def capture_logo():
    img = screenshot()
    x1 = COORD1[0] - MONITOR_LEFT
    y1 = COORD1[1] - MONITOR_TOP
    x2 = COORD2[0] - MONITOR_LEFT
    y2 = COORD2[1] - MONITOR_TOP
    return img[y1:y2, x1:x2]

#capture logo works

def is_wooly():
    current_bgr = capture_logo()
    cv2.imwrite("miscrits-logo.png", current_bgr)  # save in color

    current = cv2.cvtColor(current_bgr, cv2.COLOR_BGR2GRAY)  # gray only for matching
    ref = cv2.imread(rf"{MISCRITS_DIR}\wooly.png")
    if ref is None:
        print("❌ Could not load wooly.png")
        return False

    ref = cv2.cvtColor(ref, cv2.COLOR_BGR2GRAY)
    if ref.shape != current.shape:
        ref = cv2.resize(ref, (current.shape[1], current.shape[0]))

    score = float(cv2.matchTemplate(current, ref, cv2.TM_CCOEFF_NORMED).max())
    print(f"Wooly match score: {score:.3f}")
    return score >= THRESHOLD
'''
if __name__ == "__main__":
    import time
    time.sleep(3)
    if is_wooly():
        print("✅ It's Wooly!")
    else:
        print("❌ Not Wooly.")
'''