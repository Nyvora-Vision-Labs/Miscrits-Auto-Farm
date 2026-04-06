import mss
import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# ---- Capture monitor 2 ----
with mss.mss() as sct:
    monitor = sct.monitors[2]
    MONITOR_LEFT = monitor["left"]
    MONITOR_TOP = monitor["top"]
    screenshot = sct.grab(monitor)
    img = np.array(screenshot)
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.imwrite("game_screenshot.png", img)

print(f"Monitor 2 offset: left={MONITOR_LEFT}, top={MONITOR_TOP}")
print("Click anywhere on the image to get coordinates...\n")

# ---- Show image and capture clicks ----
fig, ax = plt.subplots(figsize=(16, 9))
ax.imshow(img_rgb)
ax.set_title("Click to get coordinates — check the console for output")

def onclick(event):
    if event.xdata is not None and event.ydata is not None:
        img_x = int(event.xdata)
        img_y = int(event.ydata)
        abs_x = MONITOR_LEFT + img_x
        abs_y = MONITOR_TOP + img_y
        print(f"Image coords: ({img_x}, {img_y})  →  Absolute screen coords: ({abs_x}, {abs_y})")
        # Draw a red dot where you clicked
        ax.plot(img_x, img_y, 'ro', markersize=6)
        fig.canvas.draw()

fig.canvas.mpl_connect('button_press_event', onclick)
plt.tight_layout()
plt.show()