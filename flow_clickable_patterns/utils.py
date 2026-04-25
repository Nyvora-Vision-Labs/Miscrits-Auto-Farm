import ctypes, time, mss, numpy as np, cv2
import random
from PIL import Image
import ctypes.wintypes

MONITOR = {"left": 1920, "top": -599, "width": 2560, "height": 1440}

def get_cursor_pos():
    """Get current cursor position."""
    pt = ctypes.wintypes.POINT()
    ctypes.windll.user32.GetCursorPos(ctypes.byref(pt))
    return pt.x, pt.y

def bezier_path(start, end, num_points=30):
    """Generate a curved path from start to end using a quadratic bezier curve."""
    sx, sy = start
    ex, ey = end

    # Random control point to create a natural curve (not a straight line)
    cx = (sx + ex) / 2 + random.randint(-80, 80)
    cy = (sy + ey) / 2 + random.randint(-80, 80)

    points = []
    for i in range(num_points + 1):
        t = i / num_points
        # Quadratic bezier formula
        x = (1 - t)**2 * sx + 2 * (1 - t) * t * cx + t**2 * ex
        y = (1 - t)**2 * sy + 2 * (1 - t) * t * cy + t**2 * ey
        points.append((int(x), int(y)))
    return points

def human_move(tx, ty):
    """Move mouse from current position to (tx, ty) along a bezier curve."""
    start = get_cursor_pos()
    path = bezier_path(start, (tx, ty), num_points=random.randint(20, 35))

    for (x, y) in path:
        ctypes.windll.user32.SetCursorPos(x, y)
        # Slightly randomized speed — faster in middle, slower at start/end
        time.sleep(random.uniform(0.008, 0.018))

    # Small overshoot correction nudge at the end (optional, feels natural)
    time.sleep(random.uniform(0.03, 0.07))
    ctypes.windll.user32.SetCursorPos(tx, ty)

def click(x, y):
    human_move(x, y)
    time.sleep(random.uniform(0.03, 0.07))
    ctypes.windll.user32.mouse_event(0x0002, 0, 0, 0, 0)  # down
    time.sleep(random.uniform(0.04, 0.09))
    ctypes.windll.user32.mouse_event(0x0004, 0, 0, 0, 0)  # up
    time.sleep(random.uniform(0.08, 0.15))

def click_random(x1, y1, x2, y2):
    min_x, max_x = min(x1, x2), max(x1, x2)
    min_y, max_y = min(y1, y2), max(y1, y2)

    tx = random.randint(min_x, max_x)
    ty = random.randint(min_y, max_y)

    human_move(tx, ty)
    time.sleep(random.uniform(0.03, 0.07))
    ctypes.windll.user32.mouse_event(0x0002, 0, 0, 0, 0)  # down
    time.sleep(random.uniform(0.04, 0.09))
    ctypes.windll.user32.mouse_event(0x0004, 0, 0, 0, 0)  # up
    time.sleep(random.uniform(0.08, 0.15))

def screenshot():
    with mss.mss() as sct:
        img = np.array(sct.grab(MONITOR))
        return cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

def matches_screen(ref_path, threshold=0.5):
    current = cv2.cvtColor(screenshot(), cv2.COLOR_BGR2GRAY)
    ref = cv2.cvtColor(cv2.imread(ref_path), cv2.COLOR_BGR2GRAY)
    if ref.shape != current.shape:
        ref = cv2.resize(ref, (current.shape[1], current.shape[0]))
    score = float(cv2.matchTemplate(current, ref, cv2.TM_CCOEFF_NORMED).max())
    print(f"Match score: {score:.3f}")
    return score >= threshold