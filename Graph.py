import numpy as np
import random
from mpl_interactions import ioff, panhandler, zoom_factory
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.wm_title("Map Building Tool v.1")

# set up the figure
fig = plt.figure(figsize=(8, 8))

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


class ScalableRectangle:
    lock = None  # only one can be animated at a time
    def __init__(self, rect):
        self.rect = rect
        self.press = None
        self.background = None

    def connect(self):
        'connect to all the events we need'
        self.cidpress = self.rect.figure.canvas.mpl_connect(
            'button_press_event', self.on_press)
        self.cidrelease = self.rect.figure.canvas.mpl_connect(
            'button_release_event', self.on_release)
        self.cidmotion = self.rect.figure.canvas.mpl_connect(
            'motion_notify_event', self.on_motion)

    def on_press(self, event):
        'on button press we will see if the mouse is over us and store some data'
        if event.inaxes != self.rect.axes: return
        if ScalableRectangle.lock is not None: return
        contains, attrd = self.rect.contains(event)
        if not contains: return
        print('event contains', self.rect.xy)
        x0, y0 = self.rect.xy
        self.press = x0, y0, event.xdata, event.ydata
        ScalableRectangle.lock = self

        # draw everything but the selected rectangle and store the pixel buffer
        canvas = self.rect.figure.canvas
        axes = self.rect.axes
        self.rect.set_animated(True)
        canvas.draw()
        self.background = canvas.copy_from_bbox(self.rect.axes.bbox)

        # now redraw just the rectangle
        axes.draw_artist(self.rect)

        # and blit just the redrawn area
        canvas.blit(axes.bbox)

    def on_motion(self, event):
        'on motion we will move the rect if the mouse is over us'
        if ScalableRectangle.lock is not self:
            return
        if event.inaxes != self.rect.axes: return
        x0, y0, xpress, ypress = self.press
        dx = event.xdata - xpress
        dy = event.ydata - ypress
        self.rect.set_x(x0+dx)
        self.rect.set_y(y0+dy)

        canvas = self.rect.figure.canvas
        axes = self.rect.axes
        # restore the background region
        canvas.restore_region(self.background)

        # redraw just the current rectangle
        axes.draw_artist(self.rect)

        # blit just the redrawn area
        canvas.blit(axes.bbox)

    def on_release(self, event):
        'on release we reset the press data'
        if ScalableRectangle.lock is not self:
            return

        self.press = None
        ScalableRectangle.lock = None

        # turn off the rect animation property and reset the background
        self.rect.set_animated(False)
        self.background = None

        # redraw the full figure
        self.rect.figure.canvas.draw()

    def disconnect(self):
        'disconnect all the stored connection ids'
        self.rect.figure.canvas.mpl_disconnect(self.cidpress)
        self.rect.figure.canvas.mpl_disconnect(self.cidrelease)
        self.rect.figure.canvas.mpl_disconnect(self.cidmotion)


#Set up the axes
axe3D = fig.add_subplot(projection='3d')

# fake data
n = 20
_x = np.arange(n)
_y = np.arange(n)
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()
top = abs(np.random.default_rng().normal(4, .1, n**2))
bottom = np.zeros_like(top)
width = depth = 1
rectangles = axe3D.bar3d(x, y, bottom, width, depth, top, shade=True, alpha=1)
print(axe3D.collections)
axe3D.set_title('Map')


srs = []
#for rect in rectangles:
#    sr = ScalableRectangle(rect)
#    sr.connect()
#    srs.append(sr)


def onclick(event):
    print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          ('double' if event.dblclick else 'single', event.button,
           event.x, event.y, event.xdata, event.ydata))

#canvas.mpl_connect('button_press_event', onclick)

def _quit():
    root.quit()
    root.destroy()

def randomize():
    top = abs(np.random.default_rng().normal(4, .1, n ** 2))
    axe3D.clear()
    axe3D.bar3d(x, y, bottom, width, depth, top, shade=True, alpha=1)
    canvas.draw()

#canvas.mpl_connect('button_press_event', randomize)

quit_button = tk.Button(master=root, text="Quit", command=_quit)
quit_button.pack(side=tk.BOTTOM)
random_button = tk.Button(master=root, text="Randomize", command=randomize)
random_button.pack(side=tk.BOTTOM)


tk.mainloop()