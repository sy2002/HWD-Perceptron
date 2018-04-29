HTML5/JavaScript client for HWD-Perceptron
==========================================

Files and folders
-----------------

The following table is sorted by importance.

|Name                  |Description
|----------------------|-------------------------------------------------------
|nn.html               |Main file that contains the HTML5 as well as the main JavaScript routines. Everything has been intentionally kept within one large HTML file for better readability when you use "View Page Source" in your browser.
|js                    |Folder with third party OpenSource JavaScript libraries: Bootstrap, JQuery, Popper and MobileDetect
|css                   |Folder with third party OpenSource CSS files: Bootswatch Cerulean Theme based on Bootstrap
|nn_mnist_examples.png |Image used by nn.html that shows sample digits
|screenshot.jpg        |Example screenshot of the client that is used by the project's main README.md
|keep_alive_ping.sh    |Currently, I am using pythonanywhere.com to host the server. They regularly send the Python server instances to sleep; this script pings the server each hour to circumvent this mechanism and to make sure, that the server is up, when somebody uses www.sy2002.de/nn.html

How it works
------------

* Bootstrap's `container-fluid` class is used to create a responsive user
  interface that scales from desktop to phone.

* There are two important named elements: `user-digits` is a HTML5 Canvas
  used to draw the digit and `nn_output` is a `<div>` of the same size as
  the Canvas to display the result.

* The net size of the Canvas is 280x280 pixels, that is 10x in each axis the
  size of the target size of 28x28 pixels (see also
  [this explanation](../server/training/#background-information) to learn
  about the training data and therefore the necessary data structures on
  the client's side): 280x280 allows the user to conveniently paint, because
  it is large enough. And it allows a higher resolution data preprocessing.

* [Line 29](nn.html#L29) defines the URL of the Python server that runs the
  Percetron Neural Network.

* When the Recognize button is pressed, then the image is preprocessed
  so that it is as similar as possible compared to the MNIST dataset.

  1. The image needs to be centered (e.g. if the user draws the
     digit in a corner instead of in the center). We use the Center of Mass
     algorithm for doing so.

  2. Then it needs to be zoomed according to the Bounding Box. This is
     necessary to handle cases, where the user draws small digits.

  3. There is an additional step that begins in [Line 290](nn.html#L290) that
     redraws all strokes ("paths") the user did for making sure, that also
     very small digits are still OK.

  4. Finally, the drawing is scaled down to 28x28 pixels and converted into
     a stream of floating point numbers ranging from -1 (white) to 1 (black).

* The REST API call to the Python server is performed asynchronously. The
  data is transmitted by concatenating the number stream that represents the
  pixels of the image to the request. Example:

  ```
  http://localhost:5000/recognize?imgdata=-1,-1,-1, ...
  ```

* The server returns a plaintext digit in `xhttp.responseText` that is then
  directly displayed by modifying the DOM as shown in
  [Line 356](nn.html#L356). In case of an error, the error is inserted into
  a named `<p>` element called `error_output`.
