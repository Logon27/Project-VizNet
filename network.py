def predict(network, input):
    output = input
    for layer in network:
        output = layer.forward(output)
    return output

def train(ui, network, loss, loss_prime, x_train, y_train, epochs = 1000, learning_rate = 0.01, errorStopThreshold = 0, verbose = True):
    import numpy as np
    for e in range(epochs):
        error = 0
        for x, y in zip(x_train, y_train):
            # forward
            output = predict(network, x)

            # error
            error += loss(y, output)

            # backward
            grad = loss_prime(y, output)
            for layer in reversed(network):
                grad = layer.backward(grad, learning_rate)

        error /= len(x_train)

        ui.progressBar.setValue(((e + 1) * 100) / epochs)

        if verbose:
            print(f"{e + 1}/{epochs}, error={error}")

        if error < errorStopThreshold:
            print("Error below threshold")
            break