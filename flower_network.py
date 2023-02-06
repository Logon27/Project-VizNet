import numpy as np
from nn import *
import re

class FlowerNetwork():

    def __init__(self, ui):
        self.ui = ui
        self.points = np.array([])
    
    def runNetwork(self, input_points, output_values, epochs, learning_rate, error_stop_threshold):
        # Don't run the network if there are no input points
        if not input_points:
            print("No Input Points")
            return

        # Reset progress bar to zero before training
        self.ui.progress_bar.setValue(0)

        X = np.reshape(input_points, (len(input_points), 2, 1))
        Y = np.reshape(output_values, (len(output_values), 1, 1))

        #unsafe alternative
        #network = eval(ui.textEdit.toPlainText())
        network_layers = self.parseInput(self.ui.text_editor.toPlainText())

        network = Network(
            network_layers,
            TrainingSet(X, Y, X, Y, np.rint),
            loss=mean_squared_error,
            loss_prime=mean_squared_error_prime,
            epochs=1,
            batch_size=1,
            layer_properties=LayerProperties(learning_rate=learning_rate, optimizer=SGD()),
            verbose=False
        )

        error_points = []
        # Epoch loop. This would normally not be necessary.
        # But I need epoch specific information for graphing purposes. Which aeronet does not currently support
        for epoch in range(epochs):
            network.train()
            accuracy_train, _ = network.test()
            # Percentage in decimal form. So 0.01 is 1%
            error_percentage = (1-accuracy_train)
            error_points.append([epoch, error_percentage])

            # Update the progress bar
            self.ui.progress_bar.setValue(round(((epoch + 1) * 100) / epochs))

            # Stop training if the error falls below the threshold
            if error_percentage < error_stop_threshold:
                break

        error_points = np.array(error_points)

        # Decision boundary plot
        points = []
        for x in np.linspace(0, 10, 20):
            for y in np.linspace(0, 10, 20):
                z = network.predict([[x], [y]])
                points.append([x, y, z[0,0]])

        self.points = np.array(points)

        # Update 3D output graph
        self.ui._3dOutputTab.canvas.updateGraph(self.points)

        # Update the heatmap if it is toggled on
        self.ui._2dGraphTab.canvas.updateHeatMap(self.points)

        # Update the error graph after training finishes
        self.ui.errorGraphTab.canvas.updateErrorGraph(error_points)

        # Set progress bar to max after training
        self.ui.progress_bar.setValue(100)
    
    def toggleHeatMap(self):
        if np.size(self.points):
            self.ui._2dGraphTab.canvas.toggleHeatMap(self.points)

    # Parses the text editor architecture into actual Network Layer Classes
    # https://stackoverflow.com/questions/553784/can-you-use-a-string-to-instantiate-a-class
    def parseInput(self, input_text):
        network_layers = []

        for line in input_text.splitlines():
            parsedLine = line.replace(" ", "")
            parsedLine = re.split('\(|,|\)', parsedLine)[:-1]
            parsedClassName = parsedLine[0]
            parsedArgs = parsedLine[1:]

            class_constructor = globals()[parsedClassName]
            if parsedClassName == "Dense":
                # input_shape, output_shape
                network_layers.append(class_constructor(int(parsedArgs[0]), int(parsedArgs[1])))
            elif parsedClassName in ["Tanh", "Sigmoid", "Relu", "LeakyRelu"]:
                network_layers.append(class_constructor())
            
        return network_layers