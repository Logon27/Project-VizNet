import numpy as np
from keras.datasets import mnist
from keras.utils import np_utils

from dense import Dense
from activations import *
from losses import mse, mse_prime
from network import train, predict

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def preprocess_data(x, y, limit):
    # reshape and normalize input data
    x = x.reshape(x.shape[0], 28 * 28, 1)
    x = x.astype("float32") / 255
    # encode output which is a number in range [0,9] into a vector of size 10
    # e.g. number 3 will become [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    y = np_utils.to_categorical(y)
    y = y.reshape(y.shape[0], 10, 1)
    return x[:limit], y[:limit]


# load MNIST from server
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, y_train = preprocess_data(x_train, y_train, 60000)
x_test, y_test = preprocess_data(x_test, y_test, 20)

# load MNIST copy for image display
(x_train_image, y_train_image), (x_test_image, y_test_image) = mnist.load_data()

# neural network
network = [
    Dense(28 * 28, 70),
    Sigmoid(),
    Dense(70, 35),
    Sigmoid(),
    Dense(35, 10),
    Sigmoid()
]

# train
train(network, mse, mse_prime, x_train, y_train, epochs=25, learning_rate=0.3)

# test
#for x, y in zip(x_test, y_test):
#    output = predict(network, x)
#    print('pred:', np.argmax(output), '\ttrue:', np.argmax(y))
    
#############################################
# added testing
# scorecard for how well the network performs, initially empty
scorecard = []

# go through all the records in the test data set
for x, y in zip(x_test[:20], y_test[:20]):
    output = x
    for layer in network:
        output = layer.forward(output)
    prediction = np.argmax(output)
    correct_label = np.argmax(y)
    print("Output: \n{}".format(output))
    print('pred:', np.argmax(output), '\ttrue:', np.argmax(y))
    # append correct or incorrect to list
    if (prediction == correct_label):
        # network's answer matches correct answer, add 1 to scorecard
        scorecard.append(1)
    else:
        # network's answer doesn't match correct answer, add 0 to scorecard
        scorecard.append(0)
    
# calculate the performance score, the fraction of correct answers
scorecard_array = np.asarray(scorecard)
print("performance = ", scorecard_array.sum() / scorecard_array.size)


fig, axes = plt.subplots(ncols=20, sharex=False, sharey=True, figsize=(20, 4))
for i in range(20):
    output = x_test[i]
    for layer in network:
        output = layer.forward(output)
    prediction = np.argmax(output)
    
    axes[i].set_title(prediction)
    axes[i].imshow(x_test_image[i], cmap='gray')
    axes[i].get_xaxis().set_visible(False)
    axes[i].get_yaxis().set_visible(False)
plt.show()