import time
import cv2
import threading
from utils import screenshot

DOUBLE_REF = "images/double.png"

# Region in screenshot coords (absolute - monitor offset)
X1, Y1, X2, Y2 = 1872, 772, 1970, 1055

THRESHOLD = 0.5

def check_double_miscrits():
    delays = [3.0,4.0]
    results = [None] * len(delays)

    ref = cv2.imread(DOUBLE_REF)
    if ref is None:
        print("❌ Could not load double.png")
        return False
    ref_crop = cv2.cvtColor(ref[Y1:Y2, X1:X2], cv2.COLOR_BGR2GRAY)

    def capture_and_check(index, delay):
        time.sleep(delay)
        img = screenshot()
        filename = f"debug_double_{index}.png"
        cv2.imwrite(filename, img)
        print(f"📸 Saved {filename}")

        current_crop = cv2.cvtColor(img[Y1:Y2, X1:X2], cv2.COLOR_BGR2GRAY)

        ref_resized = cv2.resize(ref_crop, (current_crop.shape[1], current_crop.shape[0]))
        score = float(cv2.matchTemplate(current_crop, ref_resized, cv2.TM_CCOEFF_NORMED).max())
        print(f"Double match score [{index}]: {score:.3f}")
        results[index] = score >= THRESHOLD

    threads = [
        threading.Thread(target=capture_and_check, args=(i, delay))
        for i, delay in enumerate(delays)
    ]

    for t in threads:
        t.start()
    for t in threads:
        t.join()

    return any(results)

#True if at least one of the 4 screenshots had a match score >= THRESHOLD (0.8)
#False if all of them scored below the threshold (or if double.png failed to load)

#Inner Cords
#Image coords: (1883, 783)  →  Absolute screen coords: (3803, 184)
#Image coords: (1959, 783)  →  Absolute screen coords: (3879, 184)
#Image coords: (1883, 841)  →  Absolute screen coords: (3803, 242)
#Image coords: (1962, 843)  →  Absolute screen coords: (3882, 244)