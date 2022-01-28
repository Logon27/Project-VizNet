import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from dense import Dense
from activations import Tanh
from losses import mse, mse_prime
from network import train, predict

from mplwidget2 import MplCanvas2

import re

class FlowerNetwork():

    def __init__(self, ui):
        self.ui = ui
        self.points = np.array([])
    
    def runNetwork(self, inputPoints, outputValues, epochs, learning_rate, errorStopThreshold):
        #reset progress bar to zero before training
        self.ui.progressBar.setValue(0)

        X = np.reshape(inputPoints, (len(inputPoints), 2, 1))
        Y = np.reshape(outputValues, (len(outputValues), 1, 1))

        #unsafe alternative
        #network = eval(ui.textEdit.toPlainText())
        network = self.parseInput(self.ui.textEdit.toPlainText())
        # network = [
        #     Dense(2, 3),
        #     Tanh(),
        #     Dense(3, 1),
        #     Tanh()

        #    Dense(2, 10),
        #    Tanh(),
        #    Dense(10, 5),
        #    Tanh(),
        #    Dense(5, 1),
        #    Tanh()
        # ]

        # train
        train(self.ui, network, mse, mse_prime, X, Y, epochs, learning_rate, errorStopThreshold)

        # decision boundary plot
        points = []
        for x in np.linspace(0, 10, 20):
            for y in np.linspace(0, 10, 20):
                z = predict(network, [[x], [y]])
                points.append([x, y, z[0,0]])

        self.points = np.array(points)

        #ui._2dGraphTab.canvas.
        self.ui._3dOutputTab.canvas.updateGraph(self.points)

        #update the heatmap if it is on
        self.ui._2dGraphTab.canvas.updateHeatMap(self.points)

        #set progress bar to max after training
        self.ui.progressBar.setValue(100)
    
    def toggleHeatMap(self):
        if np.size(self.points):
            self.ui._2dGraphTab.canvas.toggleHeatMap(self.points)

    def parseInput(self, inputText):
        network = []
        lineNum = 0
        for line in inputText.splitlines():
            line.replace(" ", "")
            parsedLine = re.split('\(|,|\)', line)
            if parsedLine[0].casefold() == 'Dense'.casefold():
                try:
                    layerInputSize = int(parsedLine[1])
                    layerOutputSize = int(parsedLine[2])
                    network.append(Dense(layerInputSize, layerOutputSize))
                except ValueError:
                    print('Error Parsing Architecture at line ' + lineNum)
            elif parsedLine[0].casefold() == 'Tanh'.casefold():
                network.append(Tanh())
            lineNum+=1
            #print(parsedLine)
        return network