#2D Error Widget

# Imports
from PyQt5 import QtWidgets
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
import matplotlib

# Ensure using PyQt5 backend
matplotlib.use('QT5Agg')

# Matplotlib canvas class to create figure
class MplCanvas3(Canvas):
    def __init__(self):
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        self.ax.set_xlabel('epochs')
        self.ax.set_ylabel('error')
        Canvas.__init__(self, self.fig)
        Canvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        Canvas.updateGeometry(self)

    def updateErrorGraph(self, errorPoints):
        #remove the old scatter plot if run twice
        if self.ax:
            self.ax.cla()
        self.ax.plot(errorPoints[:, 0], errorPoints[:, 1], linestyle='solid', linewidth=1, color='blue')
        self.ax.set_xlabel('epochs')
        self.ax.set_ylabel('error')
        self.figure.canvas.draw()


# Matplotlib widget
class MplWidget3(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)   # Inherit from QWidget
        self.canvas = MplCanvas3()                 # Create canvas object
        self.vbl = QtWidgets.QVBoxLayout()         # Set box for plotting
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)