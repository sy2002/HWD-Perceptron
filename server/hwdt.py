# Handwritten Digits Trainer (hwdt.py)
#
# My interpretation of the learnings from the MYONN book (by Tariq Rashid):
# A training program for the SimplePerceptronNN class that uses the handwritten
# digits dataset from MNIST (http://yann.lecun.com/exdb/mnist/) converted
# to CSV files (https://pjreddie.com/projects/mnist-in-csv/)
#
# done by sy2002 at 2nd, 7th and 8th of April 2018
#
# Some results WITHOUT data enhancement (via the "enhance_data" function):
#
# Shape [784, 500, 150, 10]         LR=0.0250   Epochs=4  => 2.86% failure
# Shape [784, 500, 200, 70, 10]     LR=0.0100   Epochs=5  => 3.44% failure (best)  Epochs=7  => 4.46%
# Shape [784, 500, 150, 10]         LR=0.0200   Epochs=10 => 2.40% failure
# Shape [784, 500, 150, 10]         LR=0.0200   Epochs=10 => 2.35% failure (best)  Epochs=16 => 2.54%
# Shape [784, 2000, 10]             LR=0.1000   Epochs=17 => 2.16% failure (best)  Epochs=19 => 2.25%
#
# Some results WITH data enhancement:
#
# Shape [784, 100, 10]              LR=0.0100   Epochs=15 => 2.49% failure (best)  Epochs=20 => 2.55%
# Shape [784, 100, 10]              LR=0.0050   Epochs=40 => 2.27% failure
# Shape [784, 100, 10]              LR=0.0040   Epochs=60 => 2.23% failure
# Shape [784, 100, 10]              LR=0.0040   Epochs=66 => 2.17% failure (best)  Epochs=83 => 2.31%
# Shape [784, 500, 150, 10]         LR=0.0100   Epochs=7  => 2.23% failure (best)  Epochs=14 => 2.67%
# Shape [784, 500, 150, 10]         LR=0.0050   Epochs=26 => 2.06% failure (best)  Epochs=39 => 2.18%
# Shape [784, 2000, 10]             LR=0.0200   Epochs=16 => 1.86% failure (best)  Epochs=17 => 1.92%

import spnn                     #Simple Perceptron Neural Network by sy2002 
from nist_csv import *          #read_csv function, specific for the NIST CSV format

import time
import numpy as np
import progressbar              #this is progressbar2, so execute: pip install progressbar2
import scipy.ndimage as ndi

# ==============================================================    
# Network, learning and input configuration
# ==============================================================

network_shape = [784, 100, 10]
learning_rate = 0.03
epochs = 1

file_save     = "test"

file_training = "training/mnist_train.csv"
file_testing  = "training/mnist_test.csv"
    
#turns one data element into three by adding a 10° to the left and to the right
#rotated version (and keeping the same label and output data)
def enhance_data(labels, outputs, handwritten_pixels):
    new_labels = []
    new_outputs = []
    enhanced_pixels = []
    for i in progressbar.progressbar(range(len(labels))):
        
        label = labels[i]
        output = outputs[i]
        pixels = handwritten_pixels[i]

        #rotate works counterclockwise, so 10° means 10° to the left
        #the reshape parameter prevents "rotated out" pixels coming in again
        #my experiments have shown, that rotate is not sticking to the range
        #of input pixels (e.g. 0.01 to 1.00), so we need to scale the output
        src = np.array(pixels).reshape(28, 28)
        rot_left = ndi.interpolation.rotate(src, 10, cval=0.01, reshape=False)
        rot_left = (rot_left / rot_left.max() * 0.99) + 0.01
        rot_right = ndi.interpolation.rotate(src, -10, cval=0.01, reshape=False)
        rot_right = (rot_right / rot_right.max() * 0.99) + 0.01

        for j in range(3):
            new_labels.append(label)
            new_outputs.append(output)
        enhanced_pixels.append(pixels)
        enhanced_pixels.append(rot_left.reshape(784))
        enhanced_pixels.append(rot_right.reshape(784))

    print("\n")
    return (new_labels, new_outputs, enhanced_pixels)

# ==============================================================    
# Main Program
# ==============================================================

print("\nHandwritten Digits Trainer by sy2002 at 8th of April 2018\n")
print("Network shape:", network_shape)
print("Learning rate: %0.4f" % learning_rate)
print("Epochs: %i\n" % epochs)

training_labels = []                #digit as an integer
training_output = []                #digit as a pattern of "0.01"s and one "0.99" for the output neurons
training_handwritten_pixels = []    #bitmap pattern of 28 x 28 = 784 input pixels

test_labels = []
test_output = []
test_handwritten_pixels = []

print("Training data is being loaded and scaled:")
(training_labels, training_output, training_handwritten_pixels) = read_csv(file_training)

print("Test data is being loaded and scaled:")
(test_labels, test_output, test_handwritten_pixels) = read_csv(file_testing)

#comment out this section, if you want to work with the unmodified input data
print("Training data is being enhanched by adding 10° left and right rotated versions:")
(training_labels, training_output, training_handwritten_pixels) = enhance_data(training_labels, training_output, training_handwritten_pixels)

nn = spnn.SimplePerceptronNN(network_shape, learning_rate)

epochs = range(epochs)
for epoch in epochs:
    print("Network is being trained (Epoch %i of %i):" % (epoch + 1, len(epochs)))
    for i in progressbar.progressbar(range(len(training_labels))):
        nn.train(training_handwritten_pixels[i], training_output[i])
    print("\n")

    #Test the success rate of the net
    success_count = 0
    for i, data in zip(test_labels, test_handwritten_pixels):
        nn_output = nn.query(data)
        if nn_output.index(max(nn_output)) == i:
            success_count += 1

    success_rate = success_count / len(test_labels)
    nn.save("saved_nn/" + file_save + "-epoch-" + str(epoch + 1), [success_rate, epoch + 1, time.time()])

    if epoch < len(epochs):
        print("Epoch %i: Current success rate: %.2f%% <==> Failure rate: %.2f%%\n" % (epoch + 1, success_rate * 100, (1 - success_rate) * 100))
    else:
        print("SUCCESS RATE OF THE NETWORK =  %.2f%% <==> FAILURE RATE = %0.2f%%\n" % (success_rate * 100, (1 - success_rate) * 100))
