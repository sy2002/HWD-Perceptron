# Simple Perceptron Neural Network (spnn.py)
#
# My interpretation of the learnings from the MYONN book (by Tariq Rashid):
# A simple but reusable multi layer Perceptron NN class. The Perceptron works without bias.
#
# Important: All input values should be normalized between 0 < input <= 1 and
#            due to the sigmoid activation function, the output is always 0 < output < 1
#
# done by sy2002 at 2nd, 7th and 8th of April 2018

import numpy as np
import sys
from scipy.special import expit

class SimplePerceptronNN:
    #layers: list [input nodes, h1, ..., hn, output nodes]; hx = amount of hidden nodes in a layer
    #learningrate is a float between 0 and 1
    #if a filename is specified, then layers and learningrate are ignored and the net is loaded instead
    def __init__(self, layers=None, learningrate=None, filename=None):
        if (layers is None) and (learningrate is None) and (filename is None):
            sys.exit("Error: No parameters given (either specify a net or load a saved net)")
        if (filename is not None):
            self.load(filename)
            return None

        self.metadata = None
        self.learningrate = learningrate
        self.layers = layers
        self._init_from_layers()

        #list of weight matrices to be interpreted like this: index i means: what are the weights,
        #that are connecting layer i-1 with i. example in a input => hidden => output 3-layer net:
        #hlayers_w[0] is empty because there are no weights connecting the input layer with
        #a non-existing previous layer; hlayers_w[1] are the weights between the input layer 0 with
        #the hidden layer 1; hlayers_w[2] are the weights connecting the hidden layer 1 with the
        #output layer 2  
        self.hlayers_w = []
        self.hlayers_w.append([])

        for i in range(1, self.count):
            inodes = self.layers[i - 1]
            onodes = self.layers[i]
            #init weight matrix, according to the book: normal distributed and limited by 1/sqrt(amount of input nodes)
            self.hlayers_w.append(np.random.normal(loc=0.0, scale=pow(inodes, -0.5), size=(onodes, inodes)))

    #use self.layers to initialize other attributes
    def _init_from_layers(self):
        self.count = len(self.layers)
        if self.count < 3:
            sys.exit("Error: At least one input layer, one hidden layer and one output layer is needed")

        self.inodes_count = self.layers[0]
        self.onodes_count = self.layers[-1]
        self.hlayers_count = self.count - 2

    #query the NN using the input list
    #input, output = 1 dimensional python standard list
    def query(self, input):
        if len(input) != self.inodes_count:
            sys.exit("Error: Wrong input vector size")

        #necessary: transform into a column vector (aka 2D matrix with one column),
        #so that it can be dot-multiplied with the weight matrix
        input = np.array(input, ndmin=2).T

        #do the actual magic: forward propagate the signal through the net
        output = []
        for i in range(1, self.count):
            #expit = sigmoid activation function; output vector = matrix x input vector
            output = expit(np.dot(self.hlayers_w[i], input))
            input = output
        return output[:, 0].tolist()

    #perform one back propagation training step using the input list and the expected output in the target list
    #input, target = 1 dimensional python standard list
    def train(self, input, target):
        if len(input) != self.inodes_count:
            sys.exit("Error: Wrong input vector size")
        if len(target) != self.onodes_count:
            sys.exit("Error: Wrong output vector size")
        
        #the array index is to be interpreted like this "what is the error *behind* this layer"
        #example in a input => hidden => output 3-layer net: errors[0] is undefined, as behind
        #input there cannot be an error; errors[1] are the errors behind the hidden layer and
        #errors[2] are the errors behind the output layer
        errors = [[] for i in range(self.count)]

        #calculate absolute error of the net at the output nodes (self.count - 1 = index of output layer)
        errors[self.count - 1] = np.array(target, ndmin=2).T - np.array(self.query(input), ndmin=2).T

        #calculate back propagated errors using the "transposed weight matrix heuristic"
        #self.count - 2 = index of the last hidden layer that is connected with the output layer
        #the range command is stopping one element before the second parameter, i.e. we will skip index 0,
        #because index 0 is the input layer and only loop back to (including) index 1
        for i in range(self.count - 2, 0, -1):
            errors[i] = np.dot(self.hlayers_w[i + 1].T, errors[i + 1])

        #we need the outputs of all layers for performing the gradient decent
        #output[0] is the input layer and therefore equals the input
        #output[i] is the output of layer i
        output = []
        output.append(np.array(input, ndmin=2).T)
        for i in range(1, self.count):
            output.append(expit(np.dot(self.hlayers_w[i], output[i - 1])))

        #adjust the weights using the gradient descent algorithm
        for i in range(1, self.count):
            self.hlayers_w[i] += self.learningrate * np.dot(
                                 errors[i] * output[i] * (1.0 - output[i]), output[i - 1].T)

    #save the network and its learning rate plus an arbitrary list of metadata
    #hlayers_w[0][0] will be used for the learning rate and hlayers_w[0][1..x] for metadata
    def save(self, filename, metadata=None):
        self.hlayers_w[0] = []
        self.hlayers_w[0].append(self.learningrate)
        if (metadata):
            for i in metadata:
                self.hlayers_w[0].append(i)
        np.savez_compressed(filename, *self.hlayers_w)
        self.hlayers_w[0] = [] #important, as we only temporarily changed it for saving

    #loads the network and sets all corresponding internal member variables (instance attributes)
    #returns a list of metadata if metadata is available, otherwise None
    def load(self, filename):
        f = np.load(filename)
        self.hlayers_w = [f[i] for i in f]
        self.learningrate = float(self.hlayers_w[0][0])

        self.metadata = None
        if len(self.hlayers_w[0]) > 1:
            self.metadata = self.hlayers_w[0][1:]

        self.hlayers_w[0] = [] #index 0 needs to be empty according to our convention (see constructor)

        #reconstruct the layers list from the matrices' shapes
        self.layers = [i.shape[1] for i in self.hlayers_w[1:]]
        self.layers.append(self.hlayers_w[-1].shape[0])
        self._init_from_layers()
