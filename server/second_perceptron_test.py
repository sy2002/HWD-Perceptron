# second_perceptron_test.py
#
# Second test of my simple perceptron:
# Create a 5 layer 4, 8, 5, 4, 2 network and teach it to output
# multiple outputs depending on certain inputs.
#
# done by sy2002 at 7th of April 2018 

import spnn

import datetime
import numpy as np
import progressbar
import timeit

training_set = [
    [[0.23, 0.09],   [0.1, 0.9, 0.7, 0.6]],         
    [[0.11, 0.07],   [0.1, 0.9, 0.7, 0.8]],         
    [[0.02, 0.12],   [0.2, 0.000001, 0.1, 0.1]],    
    [[0.23, 0.02],   [0.2, 0.000001, 0.1, 0.4]]
]

def query_it(label, net):
    print(label, "\n")
    error = 0.0
    for i, j in training_set:
        print("Query: ", j)
        o = net.query(j)
        e = np.array(i) - np.array(o)
        print("Answer: ", o, "  Error: ", e)
        error += np.sum(e**2)
    print("Error Sum: ", error)
    print("\n")

def train_it(net):
    for n in progressbar.progressbar(range(300000)):
        for answer, input in training_set:
            tc.train(input, answer)
    
tc = spnn.SimplePerceptronNN([4, 8, 5, 4, 2], 0.01)

query_it("Untrained Result:", tc)

t = timeit.Timer(lambda: train_it(tc))
sec = t.timeit(1)
print("\n\nTime needed to train:", sec, "seconds =", datetime.timedelta(seconds=sec), "\n")

query_it("Trained Result:", tc)
