Training Data for Handwritten Digits Perceptron
===============================================

About Training Data
-------------------

The Handwritten Digits Trainer (`hwdt.py`) needs training and test data in a
very specific format inside `.csv` files. Due to size restrictions of GitHub,
they cannot be part of the repository. This is why you only find a minimal
subset of the training data here in this folder: `mnist_train_100.csv` which
contains 100 training samples and `mnist_test_10.csv` which contains 10
test samples.

With these samples cannot achieve any satisfying digit recognition, but they
are good enough to test, if the network is working at all.

Install Training Data
---------------------

### Quick & Easy

**Automatic Install** (Mac and Linux only):

Go to the terminal, `cd` into the `training` folder and run `./install_data.sh`

If for some reason the file is not executable, you might need to do a
`chmod +x install_data.sh` first.


**Manual Download** (all operating systems):

You need to place the these two files into the `training` folder:

* `mnist_train.csv` (MD5: 5b49cf1b57fb9d6102b559d59d99df7c)
* `mnist_test.csv` (MD5: c807df8d6d804ab2647fc15c3d40f543)

Do not append the MD5 hash to the filename. It is given here for you to check,
if you downloaded the right files. Google for
[how to check md5](https://www.google.com/search?q=how+to+check+md5) to learn
more about how you can verify your downloads.

There are several places in the Web, where you can find the files. Here are
places that worked in April 2018, when this README.md was written:

* [mnist_train.csv Mirror #1](https://pjreddie.com/media/files/mnist_train.csv)
* [mnist_train.csv Mirror #2](http://hwdp.sy2002x.de/mnist_train.csv)
* [mnist_test.csv Mirror #1](https://pjreddie.com/media/files/mnist_test.csv)
* [mnist_test.csv Mirror #2](http://hwdp.sy2002x.de/mnist_test.csv)


**Manual Creation of the CSV Files**

1. Go to [http://yann.lecun.com/exdb/mnist/](http://yann.lecun.com/exdb/mnist/)
2. Download the four `.gz` files named `train-images-idx3-ubyte.gz`,
   `train-labels-idx1-ubyte.gz`, `t10k-images-idx3-ubyte.gz` and
   `t10k-labels-idx1-ubyte.gz`.
3. Unpack the `.gz` files into your `training` folder.
4. Run `make_csv.py`

In case LeCun's website is down, just google for the filenames. There are
plenty of places in the Web, where you can find them.

Inspecting Training Data
------------------------

To visually check, if the installation of the training data worked and if
your Python 3 stack runs fine: Go back to the project's root folder and run
`show_data.py`. It shows 10 random digits from the 60,000 digit training set
as ASCII art on stdout.

If you pass an integer as command line parameter, it is showing the given
amount of random digits.


Background Information
----------------------

[Yann LeCun et al.](http://yann.lecun.com/exdb/mnist) created a database of
handwritten digits, that has a training set of 60,000 examples, and a test set
of 10,000 examples. It is a subset of a larger set available from NIST and is
called "The MNIST Database". To my observation and today in April 2018, nearly
everybody who is doing his first steps in Machine Learning is using the MNIST
Database. I guess this is because it is extremely convenient plus since so
many people are also doing it, you can rank the results and quality (e.g.
failure rate) of your project to the rest of the pack.

The digits in the CSV files are grayscaled bitmaps that have been
size-normalized and centered in a fixed-size image of 28x28 pixels.

The format of each line of the CSV files is:

`<label><pixel 1>, <pixel 2>, ..., <pixel 784>`

`<label>` is describing the digit between 0 and 9 and `<pixel x>` is a number
between 0 and 255 that is representing a greyscale value. The pixels are
arranged in an 28x28 grid, that means that `<pixel 1>` to `<pixel 28>` are
row 1 of the digit's bitmap and `<pixel 29>` to `<pixel 57>` are row 2 and
so on.

With this information, you could also create your own learning and testing
data sets and train the network on a different basis.
