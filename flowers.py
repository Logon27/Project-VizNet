import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from dense import Dense
from activations import Tanh
from losses import mse, mse_prime
from network import train, predict

from mplwidget2 import MplCanvas2

class FlowerNetwork():

    def __init__(self, ui):
        self.ui = ui
        self.points = np.array([])
    
    def runNetwork(self, ui, inputPoints, outputValues, epochs, learning_rate):
        X = np.reshape(inputPoints, (len(inputPoints), 2, 1))
        Y = np.reshape(outputValues, (len(outputValues), 1, 1))

        network = [
            #Dense(2, 3),
            #Tanh(),
            #Dense(3, 1),
            #Tanh()

            Dense(2, 10),
            Tanh(),
            Dense(10, 5),
            Tanh(),
            Dense(5, 1),
            Tanh()
        ]

        # train
        train(network, mse, mse_prime, X, Y, epochs, learning_rate)

        # decision boundary plot
        points = []
        for x in np.linspace(0, 10, 20):
            for y in np.linspace(0, 10, 20):
                z = predict(network, [[x], [y]])
                points.append([x, y, z[0,0]])

        self.points = np.array(points)

        #ui._2dGraphTab.canvas.
        ui._3dOutputTab.canvas.updateGraph(self.points)
    
    def toggleHeatMap(self):
        if np.size(self.points):
            self.ui._2dGraphTab.canvas.toggleHeatMap(self.points)
    