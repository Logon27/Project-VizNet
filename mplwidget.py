# Imports
from PyQt5 import QtWidgets
from matplotlib.backend_bases import MouseEvent
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
import matplotlib
import numpy as np

import random

# Ensure using PyQt5 backend
matplotlib.use('QT5Agg')

# Matplotlib canvas class to create figure
class MplCanvas(Canvas):
    def __init__(self):
        #stores the x, y, output values for the neural network
        self.inputPoints = []
        #red = 0, blue = 1 for the outputs
        self.outputValues = []
        #stores the scatter plot points so they can visibly be removed
        self.scatterpoints = []
        self.fig = Figure()
        self.axes = self.fig.add_subplot(111)
        self.axes.set_xlim(0,10)
        self.axes.set_ylim(0,10)
        self.fig.canvas.mpl_connect('button_press_event', self.on_mouse_click)
        Canvas.__init__(self, self.fig)
        Canvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        Canvas.updateGeometry(self)
    
    #for debugging only
    #def onclick(self, event):
    #    print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %('double' if event.dblclick else 'single', event.button, event.x, event.y, event.xdata, event.ydata))
        
    def on_mouse_click(self, event):
        #left click (red, 0)
        if event.button == 1:
            self.inputPoints.append([event.xdata,event.ydata])
            self.outputValues.append([0])
            self.scatterpoints.append(self.axes.scatter(event.xdata, event.ydata, color='red'))
        #middle click
        elif event.button == 2:
            for i in range(0,10):
                #generate random x, y values
                x = random.uniform(0, 10)
                y = random.uniform(0, 10)
                self.inputPoints.append([x,y])
                self.outputValues.append([0])
                self.scatterpoints.append(self.axes.scatter(x, y, c='red'))

                #generate second set of random x, y values
                x = random.uniform(0, 10)
                y = random.uniform(0, 10)
                self.inputPoints.append([x,y])
                self.outputValues.append([1])
                self.scatterpoints.append(self.axes.scatter(x, y, c='blue'))
        #right click (blue, 1)
        elif event.button == 3:
            self.inputPoints.append([event.xdata,event.ydata])
            self.outputValues.append([1])
            self.scatterpoints.append(self.axes.scatter(event.xdata, event.ydata, color='blue'))
        #draw the image. must be redrawn with every change. it does not happen automatically
        self.figure.canvas.draw()
    
    def clearGraph(self):
        #self.getGraphValues()
        #remove all the points one by one
        for point in self.scatterpoints:
            point.remove()
        #clear the input/output lists
        self.inputPoints.clear()
        self.outputValues.clear()
        #clear the point list
        self.scatterpoints.clear()
        #redraw the image.
        self.figure.canvas.draw()
    
    def getGraphValues(self):
        #print(self.inputPoints)
        #print(self.outputValues)
        return self.inputPoints, self.outputValues

# Matplotlib widget
class MplWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)   # Inherit from QWidget
        self.canvas = MplCanvas()                  # Create canvas object
        self.vbl = QtWidgets.QVBoxLayout()         # Set box for plotting
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)