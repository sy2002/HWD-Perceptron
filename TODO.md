Stub for server/README.md

### Flexible Python Perceptron Class

The heart of this project is the flexible Python Perceptron class called
`SimplePerceptronNN` and located in [spnn.py](server/spnn.py). It can not
only be used for learning to recognize handwritten digits, but it can be
used for "anything".

`SimplePerceptronNN` allows a flexible layout of the network by specifying
the input nodes, the hidden nodes and the output nodes within a simple
Python list. The following pseudo-code is illustrating this:

```python
import spnn

learning_rate = 0.1
nn = spnn.SimplePerceptronNN([784, 100, 10], learning_rate)

# you need a deeper network? try this:
# nn = spnn.SimplePerceptronNN([784, 2000, 500, 250, 100, 10], learning_rate)

for t, o in zip(training, desired_output):
    nn.train(t, o)

# network is now ready to answer questions:
output = nn.query(the_input)    
```
