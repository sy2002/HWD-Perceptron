# first_perceptron_test.py
#
# First test of my simple perceptron:
# Create a 4 layer 4-3-3-2 network and teach it to output [0.2, 0.3]
# when the input is [0.1, 0.2, 0.3, 0.4]
#
# done by sy2002 at 7th of April 2018 

import spnn

print("\nSimple 4-3-3-2 perceptron network being trained to learn,")
print("that the input vector [0.1, 0.2, 0.3, 0.4] shall output [0.2, 0.3]")
print("done by sy2002 at 7th of April 2018\n")

tc = spnn.SimplePerceptronNN([4, 3, 3, 2], 0.1)

result = tc.query([0.1, 0.2, 0.3, 0.4])
print("Untrained Result:\n", result, "\n")

for i in range(0, 1000):
    tc.train([0.1, 0.2, 0.3, 0.4], [0.2, 0.3])

print("Trained Result (1,000 iterations):\n", tc.query([0.1, 0.2, 0.3, 0.4]), "\n")

for i in range(0, 10000):
    tc.train([0.1, 0.2, 0.3, 0.4], [0.2, 0.3])

print("Trained-Result (additional 10,000 iterations):\n", tc.query([0.1, 0.2, 0.3, 0.4]), "\n")

print("\nFinal weights\n")
for i in range(0, tc.count):
    print("**** Weights layer ", i, "****\n", tc.hlayers_w[i])
