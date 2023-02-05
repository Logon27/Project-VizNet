from PyQt5 import QtWidgets
from dialog import Ui_MainWindow
from flower_network import FlowerNetwork
import sys

#Start venv

#cd into Workspace/TIC Neural Network/

#.\venvNeuralNetwork\Scripts\activate.bat

#stop exit venv...
#deactivate


#Make changes in QT Designer

#add a widget placeholder to the tab in qt designer
#right click and promote
#MplWidget promoted class name. And mplwidget header file

#inside the mplwidget python file is where you will actually make matplotlib changes.

#mplwidget



#Compile with...
#pyuic5 dialog.ui > dialog.py

#The run... python application.py

###===============================###

#TODO:

#3d gradient descent plot
#https://jackmckew.dev/3d-gradient-descent-in-python.html

#Abandoned the network architecture diagram and added a network designer instead via text

#need to pass the self.ui UI element to all widgets and classes.
#https://stackoverflow.com/questions/38010391/share-python-objects-between-two-or-more-py-files

#I could just pass self.ui.progressBar into the constructor of the clearGraph function in this class.
#Then I could clear it in the widget

#https://dawes.wordpress.com/2014/06/27/publication-ready-3d-figures-from-matplotlib/
#awesome looking 3d plot with 2d projection

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        flower_network = FlowerNetwork(self.ui)
        # EVENT HANDLING
        # Register the clear_graph_button
        self.ui.clear_graph_button.clicked.connect(lambda: self.ui._2dGraphTab.canvas.clearGraph())
        self.ui.heatmap_toggle.clicked.connect(lambda: flower_network.toggleHeatMap())
        # * in front unpacks the tuple as arguments
        # Might want to create a FlowerNetwork object here then just pass the function to it. 
        # So its not anonymous every time and can be saved
        self.ui.start_training_button.clicked.connect(
            lambda: flower_network.runNetwork(*self.ui._2dGraphTab.canvas.getGraphValues(), self.ui.epochs_box.value(), self.ui.learning_rate_box.value(), self.ui.error_stop_box.value()))

        # Setting the default test of the network architecture window
        # The weird indentation is a quirk of python multiline strings
        self.ui.text_editor.setPlainText(
"""Dense(2, 20)
Tanh()
Dense(20, 10)
Tanh()
Dense(10, 1)
Tanh()""")
    
    def getEpochValue(self):
        return self.ui.epochs_box.value()

    def getLearningRateValue(self):
        return self.ui.learning_rate_box.value()


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()


#Make changes in QT Designer

#add a widget placeholder to the tab in qt designer
#right click and promote
#MplWidget promoted class name. And mplwidget header file

#inside the mplwidget python file is where you will actually make matplotlib changes.

#mplwidget

#Compile with...
#pyuic5 dialog.ui > dialog.py

#The run... python application.py




#Helpful links
#https://stackoverflow.com/questions/43947318/plotting-matplotlib-figure-inside-qwidget-using-qt-designer-form-and-pyqt5
#https://www.pythonguis.com/tutorials/embed-pyqtgraph-custom-widgets-qt-app/
#https://matplotlib.org/stable/users/explain/event_handling.html





#OLD TODO TASKS

#https://stackoverflow.com/questions/7821518/matplotlib-save-plot-to-numpy-array
#figure out how to convert the matplotlib scatter plot to a numpy array for the network to intake
#DONE

#https://stackoverflow.com/questions/33282368/plotting-a-2d-heatmap-with-matplotlib
#convert to a heatmap
#Z = np.random.rand(5, 5) 
#self.axes.pcolormesh(Z, zorder=0)

#https://github.com/martisak/dotnets
#likely requires graphicviz to compile.
#add methods to the network, layer, and dense classes to get the input and output sizes of each dense layer.
#then take the dotnets code and modify the layers array at the top.
#compile the picture to the local directory and display it within the program window.