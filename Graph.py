import numpy
import numpy as np
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.pyplot as plt
import tkinter as tk

class MapGraph(FigureCanvasTkAgg):
    def __init__(self, container, heights, length, width, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # set up the figure
        fig = plt.figure(figsize=(8, 8))

        self.canvas = FigureCanvasTkAgg(fig, master=container)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=0, column=0)

        self.toolbarFrame = tk.Frame(container)
        self.toolbarFrame.grid(row=1, column=0)
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.toolbarFrame)
        self.toolbar.update()

        self.quit_button = tk.Button(master=container, text="Quit", command=self._quit)
        self.quit_button.grid(row=2, column=0)

        #Set up the axes
        self.axe3D = fig.add_subplot(projection='3d')

        # fake data
        self.n_x = width
        self.n_y = length
        _x = np.arange(self.n_x)
        _y = np.arange(self.n_y)
        _xx, _yy = np.meshgrid(_x, _y)
        self.x, self.y = _xx.ravel(), _yy.ravel()
        self.top = numpy.array(heights)
        self.bottom = np.zeros_like(self.top)
        self.width = self.depth = 1
        rectangles = self.axe3D.bar3d(self.x, self.y, self.bottom, self.width, self.depth, self.top, shade=True, alpha=1)
        self.axe3D.set_title('Map')

    def _quit(self):
        self.canvas.get_tk_widget().grid_forget()
        self.toolbarFrame.grid_forget()
        self.quit_button.grid_forget()
