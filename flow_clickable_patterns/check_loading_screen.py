import time
import cv2
import threading
from utils import matches_screen, screenshot

LOADING_REF = "images/loading_page_2.png"

def check_loading_screen():
    
    delays = [0.77,0.82, 0.85, 0.90]
    results = [None] * len(delays)

    def capture_and_check(index, delay):
        time.sleep(delay)
        img = screenshot()
        filename = f"debug_screenshot_{index}.png"
        #cv2.imwrite(filename, img)
        print(f"📸 Saved {filename}")
        results[index] = matches_screen(LOADING_REF)

    threads = [
        threading.Thread(target=capture_and_check, args=(i, delay))
        for i, delay in enumerate(delays)
    ]

    for t in threads:
        t.start()
    for t in threads:
        t.join()

    return any(results)