from pynput import mouse

def on_click(x, y, button, pressed):
    if pressed:
        print(f"Clicked at: ({x}, {y})")
        # Stop after first click if you want:
        return False

with mouse.Listener(on_click=on_click) as listener:
    print("Click anywhere on the screen...")
    listener.join()