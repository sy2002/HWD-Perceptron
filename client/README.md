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
  used to draw the digit and `rec_hl` is a `<div>` of the same size as
  the Canvas to display the result.
* The net size of the Canvas is 280x280 pixels, that is 10x in each axis the
  size of the target size of 28x28 pixels (see also
  [this explanation](../server/training/#background-information) to learn
  about the training data and therefore the necessary data structures on
  the client's side).