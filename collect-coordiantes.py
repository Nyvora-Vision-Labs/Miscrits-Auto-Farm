import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread("game_screenshot.png")

fig, ax = plt.subplots()
ax.imshow(img)

def onclick(event):
    if event.xdata and event.ydata:
        print(f"Clicked at: x={int(event.xdata)}, y={int(event.ydata)}")

cid = fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()

#chest locations: 
#Clicked at: x=1311, y=663
#Clicked at: x=1333, y=576
#Clicked at: x=1241, y=572

#miscrit image location:
#Clicked at: x=1572, y=83
#Clicked at: x=1576, y=96

#attack location:
#Clicked at: x=850, y=1297

#miscrit color:
#Clicked at: x=1547, y=58

#continue:
