TODO: Improve the README.md documentation by the following chapters (see
below). After that: Create a README.md in the server and client folder.

How does it work?
-----------------

### Basic principle

XYZ ABC

Python Server and HTML5/JavaScript client and refer to README.md in the
server and the client folder to directly navigate there for more details.
In the server's README.md also link to the training's README.md

Picture of the net?

### Server

XYZ

Scroll back in the server terminal: See ASCII art and recognition

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

Tinkering
---------

In case you installed the project manually, just navigate to the root folder
of the project to start tinkering.

In case you used Docker, execute bash when starting the image and navigate
to /opt/HWD-Perceptron:

```
docker run -it -p 5000:5000 sy2002/hwd-perceptron /bin/bash
cd /opt/HWD-Perceptron
```

### Inspect the training data

show-data script with command line param to show 25 ASCII arts.

### Increasing the recognition accuracy

For saving time during the installation process, only a suboptimally trained
network is being created. Training a network well takes significant time.

...

Experiment with better recognition rate, try XYZ file that is part of the
package:

Or train a better network by yourself by following these steps:

1. akd sdfkl lkj dfkslj 

2. dfjlskd fslkj dfkls f

3. sdkaslkdjasjlkd

### Invoking the REST API

using the browser console output (press alt+cmd+k on firefox mac, browser
and OS specific) to generate a link that can be used to query the rest API
of the server

