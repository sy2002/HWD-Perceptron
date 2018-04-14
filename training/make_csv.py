#!/usr/bin/env python

# This converter was written by Joseph Chet Redmon
# I found it on https://pjreddie.com/projects/mnist-in-csv/
#
# slightly modified for the HWD Perceptron project's needs
# by sy2002 in April 2018

import sys

def convert(imgf, labelf, outf, n):
    f = open(imgf, "rb")
    o = open(outf, "w")
    l = open(labelf, "rb")

    f.read(16)
    l.read(8)
    images = []

    for i in range(n):
        image = [ord(l.read(1))]
        for j in range(28*28):
            image.append(ord(f.read(1)))
        images.append(image)

    for image in images:
        o.write(",".join(str(pix) for pix in image)+"\n")
    f.close()
    o.close()
    l.close()

if sys.version_info <= (3, 0):
    sys.stdout.write("The HWD Perceptron project needs Python 3\n")
    sys.exit(1)

print("This converter creates mnist_train.csv and mnist_test.csv from")
print("raw data found on http://yann.lecun.com/exdb/mnist/")
print("\nPlease be patient, this might take a bit...")

convert("train-images-idx3-ubyte", "train-labels-idx1-ubyte",
        "mnist_train.csv", 60000)
convert("t10k-images-idx3-ubyte", "t10k-labels-idx1-ubyte",
        "mnist_test.csv", 10000)

print("\nTo check, if the script was successful, use MD5.\n")
print("mnist_train.csv   MD5: 5b49cf1b57fb9d6102b559d59d99df7c")
print("mnist_test.csv    MD5: c807df8d6d804ab2647fc15c3d40f543")
print("")
