import mss
import cv2
import numpy as np

# -----------------------------
# STEP 1: Capture screen
# -----------------------------
with mss.mss() as sct:
    monitor = sct.monitors[2]  # 1 = main screen

    screenshot = sct.grab(monitor)

    # Convert to numpy array
    img = np.array(screenshot)

    # Convert BGRA -> BGR (for OpenCV)
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

    # Save image
    cv2.imwrite("game_screenshot.png", img)

print("✅ Screenshot saved as game_screenshot.png")