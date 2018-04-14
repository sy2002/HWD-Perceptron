#!/usr/bin/env python

# Visual test app to output ASCII art based on "mnist_train.csv"
# 
# If no command line parameter is given, 10 random digits from the training
# set are printed to stdout otherwise the command line parameter is
# interpreted as the amount of random digits to be printed.
#
# done by sy2002 at April, 14th 2018

from nist_csv import *

import os.path
import random
import sys

DATA_SOURCE = "training/mnist_train.csv"

print("Visual test app to output ASCII art based on training data")
print("done by sy2002 at April, 14th 2018\n")

if not os.path.isfile(DATA_SOURCE):
    print(DATA_SOURCE, "not found.")
    print("Please follow the instructions in training/README.md")
    sys.exit()

if sys.version_info <= (3, 0):
    sys.stdout.write("The HWD Perceptron project needs Python 3\n")
    sys.exit()
    
if len(sys.argv) == 2:
    amount = int(sys.argv[1])
else:
    amount = 10

print("Reading data:")
(labels, output, pixels) = read_csv(DATA_SOURCE)

for i in range(amount):
    row = random.randint(0, 59999)
    ascii_art_debug_output(pixels[row], labels[row])
