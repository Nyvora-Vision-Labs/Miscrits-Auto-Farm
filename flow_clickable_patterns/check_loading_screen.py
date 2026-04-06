import time
import cv2
from utils import matches_screen, screenshot

LOADING_REF = "images/loading_page_2.png"

def check_loading_screen():
    for i, delay in enumerate([0.5, 0.7, 0.9], start=1):
        time.sleep(delay)

        # Capture screenshot using your existing function
        img = screenshot()

        # Save debug image
        filename = f"debug_screenshot_{i}.png"
        cv2.imwrite(filename, img)
        print(f"📸 Saved {filename}")

        # Run matching
        if matches_screen(LOADING_REF):
            return True

    return False