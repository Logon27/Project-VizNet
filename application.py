from PyQt5 import QtWidgets
from dialog import Ui_MainWindow
from flowers import FlowerNetwork
import sys

#TODO:
#https://stackoverflow.com/questions/7821518/matplotlib-save-plot-to-numpy-array
#figure out how to convert the matplotlib scatter plot to a numpy array for the network to intake

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #EVENT HANDLING
        #register the clearGraphButton
        self.ui.clearGraphButton.clicked.connect(lambda: self.ui._2dGraphTab.canvas.clearGraph())
        #* in front unpacks the tuple as arguments
        #Might want to create a FlowerNetwork object here then just pass the function to it. 
        #So its not anonymous every time and can be saved
        self.ui.startTrainingButton.clicked.connect(
            lambda: FlowerNetwork().runNetwork(*self.ui._2dGraphTab.canvas.getGraphValues(), self.ui.epochsBox.value(), self.ui.learningRateBox.value()))
    
    def getEpochValue(self):
        return self.ui.epochsBox.value()

    def getLearningRateValue(self):
        return self.ui.learningRateBox.value()


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

#The run python application2.py




#Helpful links
#https://stackoverflow.com/questions/43947318/plotting-matplotlib-figure-inside-qwidget-using-qt-designer-form-and-pyqt5
#https://www.pythonguis.com/tutorials/embed-pyqtgraph-custom-widgets-qt-app/
#https://matplotlib.org/stable/users/explain/event_handling.html