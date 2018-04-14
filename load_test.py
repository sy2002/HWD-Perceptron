# load_test.py
#
# Loads a NN and tests it against the test data set.
# Expects that the first metadata element is the success rate of the NN, so
# that we can see, if it is equal to the success rate when it was saved
#
# done by sy2002 on 8th of April 2018

import spnn
from nist_csv import *

import datetime
import sys

print("\nSimplePerceptronNN Load Test, done by sy2002 at 8th of April 2018")

if len(sys.argv) != 3:
    print("usage: python load_test.py <name of the network to load> <test data>\n")
    sys.exit()

nn = spnn.SimplePerceptronNN(filename=sys.argv[1])
print("\nLayers: ", nn.layers)
success = float(nn.metadata[0]) * 100
print("Success rate: %.2f%%  <==> Failure rate: %.2f%%" % (success, 100 - success))
print("Creation date: %s (Epoch: %i)\n" % (str(datetime.datetime.fromtimestamp(int(nn.metadata[2]))), int(nn.metadata[1])))

print("Test data is being loaded and scaled:")
(test_labels, test_output, test_handwritten_pixels) = read_csv(sys.argv[2])

print("Test is being performed:")
count_success = 0
count_all = len(test_labels)
for i in progressbar.progressbar(range(count_all)):
    nn_output = nn.query(test_handwritten_pixels[i])
    if nn_output.index(max(nn_output)) == test_labels[i]:
        count_success +=1
print("\n")

actual_success = count_success / count_all * 100
print("Actual success rate: %.2f%%  <==> Actual failure rate: %.2f%%" % (actual_success, 100 - actual_success))
if (actual_success == success):
    print("NETWORK IS OK")
else:
    print("!! NETWORK IS NOT OK !!")

print()