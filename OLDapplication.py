from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

from matplotlib import pyplot

Form, Window = uic.loadUiType("dialog.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
app.exec()

#might be able to just webscrape for the network diagram
#http://alexlenail.me/NN-SVG/index.html

#https://github.com/martisak/dotnets

#this File is no longer used