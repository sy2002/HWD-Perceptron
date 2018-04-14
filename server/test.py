# first steps towards the handwritten digits hello world sample
# done by sy2002 on April, 1st 2018
# goals: create perceptron logic NN in a dynamic manner: input the shape of the net,
# test the calculation of the net's output using repeated matrix x vector multiplications

import numpy as np
import sys

from scipy.special import expit

class Test:

    def __init__(self, layers):
        self.count = len(layers)
        if self.count < 3:
            sys.exit("Error: At least one input layer, one hidden layer and one output layer is needed")

        self.layers = layers
        self.inodes_count = layers[0]
        self.onodes_count = layers[self.count - 1]
        self.hlayers_count = self.count - 2        
        self.hlayers_w = []

        self.hlayers_w.append([])
        for i in range(1, self.count):
            inodes = self.layers[i - 1]
            hnodes = self.layers[i]
            #init weight matrix, according to the book: normal distributed and limited by 1/sqrt(amount of input nodes)
            self.hlayers_w.append(np.random.normal(loc=0.0, scale=pow(inodes, -0.5), size=(hnodes, inodes)))

    def query(self, input):
        if len(input) != self.inodes_count:
            sys.exit("Error: Wrong input vector size")
        input = np.array(input, ndmin=2).T #necessary: transform into a column vector
        output = []
        for i in range(1, self.count):
            print("======\n", self.hlayers_w[i], "\n", input, "\n******")
            #expit = sigmoid function; output vector = matrix x input vector
            output = expit(np.dot(self.hlayers_w[i], input))
            print(output)
            print("!!!!!!")
            input = output
        return output
            

tc = Test([4, 3, 2])

print(tc.count)
print(tc.hlayers_w[0])
print(tc.hlayers_w[1])
print(tc.hlayers_w[2])

print(tc.query([1, 2, 3, 4]))
