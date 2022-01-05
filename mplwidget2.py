#3D Graph Widget

# Imports
from PyQt5 import QtWidgets
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
import matplotlib

# Ensure using PyQt5 backend
matplotlib.use('QT5Agg')

# Matplotlib canvas class to create figure
class MplCanvas2(Canvas):
    def __init__(self):
        self.scatter = None
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111, projection="3d")
        Canvas.__init__(self, self.fig)
        Canvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        Canvas.updateGeometry(self)

    def updateGraph(self, points):
        #remove the old scatter plot if run twice
        if self.scatter:
            self.scatter.remove()
        self.scatter = self.ax.scatter(points[:, 0], points[:, 1], points[:, 2], c=points[:, 2], cmap=matplotlib.cm.get_cmap('seismic_r'))
        self.figure.canvas.draw()


# Matplotlib widget
class MplWidget2(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)   # Inherit from QWidget
        self.canvas = MplCanvas2()                 # Create canvas object
        self.vbl = QtWidgets.QVBoxLayout()         # Set box for plotting
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)