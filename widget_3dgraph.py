#3D Graph Widget

# Imports
from PyQt5 import QtWidgets
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
import matplotlib

# Ensure using PyQt5 backend
matplotlib.use('QT5Agg')

# Matplotlib canvas class to create figure
class MplCanvas3dGraph(Canvas):
    def __init__(self):
        self.scatter = None
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111, projection="3d")
        self.ax.set_xlabel('Width Of Flower Petal')
        self.ax.set_ylabel('Length Of Flower Petal')
        self.ax.set_zlabel('Network Prediction')
        self.fig.patch.set_facecolor('0.4')
        self.ax.patch.set_facecolor('0.4')
        Canvas.__init__(self, self.fig)
        Canvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        Canvas.updateGeometry(self)

    def updateGraph(self, points):
        # Remove the old scatter plot if run twice
        if self.scatter:
            self.scatter.remove()
        self.scatter = self.ax.scatter(points[:, 0], points[:, 1], points[:, 2], c=points[:, 2], cmap=matplotlib.cm.get_cmap('seismic_r'))
        self.figure.canvas.draw()


# Matplotlib widget
class Widget3dGraph(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)   # Inherit from QWidget
        self.canvas = MplCanvas3dGraph()           # Create canvas object
        self.vbl = QtWidgets.QVBoxLayout()         # Set box for plotting
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)