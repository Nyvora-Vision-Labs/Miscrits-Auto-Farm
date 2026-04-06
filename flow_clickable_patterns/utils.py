import ctypes, time, mss, numpy as np, cv2

MONITOR = {"left": 1920, "top": -599, "width": 2560, "height": 1440}

def click(x, y):
    ctypes.windll.user32.SetCursorPos(int(x), int(y))
    time.sleep(0.05)
    ctypes.windll.user32.mouse_event(0x0002, 0, 0, 0, 0)
    time.sleep(0.05)
    ctypes.windll.user32.mouse_event(0x0004, 0, 0, 0, 0)
    time.sleep(0.1)

def screenshot():
    with mss.mss() as sct:
        img = np.array(sct.grab(MONITOR))
        cv2.imwrite("debug_screenshot.png", img)
        return cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

def matches_screen(ref_path, threshold=0.5):
    current = cv2.cvtColor(screenshot(), cv2.COLOR_BGR2GRAY)
    ref = cv2.cvtColor(cv2.imread(ref_path), cv2.COLOR_BGR2GRAY)
    if ref.shape != current.shape:
        ref = cv2.resize(ref, (current.shape[1], current.shape[0]))
    score = float(cv2.matchTemplate(current, ref, cv2.TM_CCOEFF_NORMED).max())
    print(f"Match score: {score:.3f}")
    return score >= threshold