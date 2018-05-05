Python Server for HWD-Perceptron
==========================================

Files and folders
-----------------

The following table is sorted by importance.

|Name                      |Description
|--------------------------|-------------------------------------------------------
|spnn.py                   |Simple Perceptron Neural Network: This is the main workhorse of the whole project. A Python class called `SimplePerceptronNN`, that implements a freely configurable Perceptron based Neural Network; you can specify the amount of nodes for each layer. Besides the obligatory training and querying features, the class also features saving and loading of networks including metadata.
|hwdr_server.py            |Flask based REST API server: It uses loads a previously trained network, receives requests via REST and outputs the recognized digit.
|hwdt.py                   |Training tool: Uses CSV based training data and runs multiple epochs to train handwritten digits recognition networks. Each epoch is saved as a separate file and metadata is added, so that later, after possibly long running training sessions, the best network version can be selected.
|nist_csv.py               |Helper functions: Load and parse CSV files in our [special format](training#background-information). Additionally an elegant ASCII art printing function is included.
|load_test.py              |Test program that checks loads a neural network and tests, if it performs according to the metadata stored within the file. This tool is a good test for the whole Python and training stack because it actually tests, if everything works as expcted.
|test_cp.py                |Tinkering tool: You can copy/paste the web browser console output of the [client](../client/nn.html) and test, if the recognition works as expected. See also the [tinkering section](../README.md#running-the-classification-manually-as-python-script) in the main README.md.
|training                  |Folder that stores training data. There is a [README.md](training) there worth reading.
|saved_nn                  |Folder that contains networks, that I experimented with. Have a look at the [training results](hwdt.py#L10) to learn more about them and to choose, which one you might want to test. The folder also contains by default all networks that you generate with `hwdt.py`.
|first_perceptron_test.py  |This was the development testbed I used while developing `SimplePerceptronNN (spnn.py)`. It trains a network with 4 input nodes, 2 hidden layers with 3 nodes each and 2 output nodes to output a certain value pair given certain inputs.
|second_perceptron_test.py |After `first_perceptron_test.py` worked, I used this more advanced development testbed to check, if deeper networks are working (I used [4, 8, 5, 4, 2]) and if this "low node count but deep" network could learn an [excercise](second_perceptron_test.py#L16), that is a bit more complex. I also used this to get a first idea about learning times and CPU power requirements.
|second_perceptron_test.txt|Results achieved with `second_perceptron_test.py`.

SimplePerceptronNN: Flexible Python Perceptron Class
----------------------------------------------------

The heart of this project is the flexible Python Perceptron class called
`SimplePerceptronNN` and located in [spnn.py](spnn.py). It can not
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

# make sure that the length of the 'training' list equals the amount of input
# nodes and the length of 'desired_output' equals the amount of output nodes
for t, o in zip(training, desired_output):
    nn.train(t, o)

# network is now ready to answer questions:
output = nn.query(the_input)    
```

### Design Decisions

* The network can be arbitrarily big and/or deep. But keep in mind that the
  code is CPU-only code (no GPU acceleration), so it quickly becomes pretty
  CPU and RAM hungry.

* I decided not to use any [bias](https://en.wikipedia.org/wiki/Perceptron#Definition),
  because after all, this class is called *Simple* Perceptron Neural Network.
  And it works pretty well - even without a bias.

* For a similar reason, I am using the [Sigmoid Function](https://en.wikipedia.org/wiki/Sigmoid_function):
  as activation function: I wanted to work through the math behind creating
  the backpropagation algorithm by myself (which includes calculating partial
  derivatives of it to obtain the gradient and then simplifying and
  transforming it all to be doable in pure matrix multiplications) and it
  seemed to me, that the Signmoid Function is "kind of easy but still hard
  enough" for me personally and my current state of learning to actually
  be able to do it. I know, that other functions would work better.


