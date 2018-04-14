# nist_csv.py
#
# Read CSV with training or test data and return a tuple of lists:
# ([labels as integer values], [labels friendly for the output nodes], [784 input pixels of bitmap data])
# the input pixels are scaled between 0.01 and 1.00 to satisfy the constraints of spnn.SimplePerceptronNN
# the output neuron patters respect the constraint, that the maximum output is < 1
#
# Additionally, there is an ASCII art print function for the 28x28 pixel digits
#
# done by sy2002 on 7th and 8th of April 2018

import csv
import numpy as np
import progressbar

def read_csv(file_name):
    labels = []
    output = []
    handwritten_pixels = []

    reader = csv.reader(open(file_name), delimiter=",")
    lines = list(reader)

    for i in progressbar.progressbar(lines):
        label = int(i[0])
        labels.append(label)

        #create output neuron pattern: a list of 10 elements consisting of 0.01s
        #and at the position of the right digit, place a 0.99
        output.append([0.01 if n != int(i[0]) else 0.99 for n in range(10)])

        #scale the input pattern from 0..255 to 0.01..1.0
        handwritten_pixels.append((np.asfarray(i[1:]) / 255.0 * 0.99) + 0.01)

    print("\n")
    return (labels, output, handwritten_pixels)

#convert the bitmap given by pixels to a ASCII art greyscale of 10 "tones" and print it
def ascii_art_debug_output(pixels, label=None):
    print("=============================")
    if label is not None:
        print("             ", label)
        print("=============================")
    ascii_art_converter=" .:-=+*#%@"
    ascii_art_indexrange = len(ascii_art_converter) - 1
    for l in np.array(pixels).reshape(28, 28):
        for c in l:
            print(ascii_art_converter[int(float(c) * ascii_art_indexrange)], end="")
        print("")
    print("=============================\n")
