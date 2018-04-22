Manual installation of dependencies
===================================

The following hints are geared towards a clean and minimal Ubuntu 16.04 LTS,
for example the one that you get when you run

```
docker run -it -p 5000:5000 ubuntu:16.04
```

The port mapping is shown here for your convenience, because when you use
Docker to run this version of Ubuntu and the port mapping is already done,
then you can later, when you followed these instructions also use the
container as HWD-Perceptron server.

Also if you do not use Ubuntu: This guide gives you a good idea about the
dependencies that are necessary for running HWD-Perceptron.

Dependencies
------------

1. git
2. curl or wget
3. Python 3.6 (or newer) being installed, so that `python` yields the
   Python 3.6 installation and not Python 2
4. pip for Python 3.6 being installed, so that `pip` yields the pip for
   Python 3.6 and not Python 2
5. Venv for Python 3.6 (Virtual Environment)

If you can satisfy the dependencies (3) and (4), then you do not
necessarily need to run the system inside a Virtual Environment. The
following installation is not installing any `python` command but only
a `python3` command, and therefore the Virtual Environment is needed.

Step-by-step guide for the minimal Ubuntu 16.04 LTS
---------------------------------------------------

Hint: Depending on your actual operating system installation, the
below-mentioned `apt-get` commands need to be prefixed with `sudo`.

### Step 1: git, curl and some common dependencies

```
apt-get update
apt-get install git curl
apt-get install software-properties-common
```

After these dependencies have been installed, you can check your Ubuntu
version by running

```
lsb_release -a
```

### Step 2a: Install old Python 3

The repos of Ubuntu 16.04 contain an older version of Python 3. On my machine
it was Python 3.5.2.

```
apt-get install python3 python3-pip
apt-get install python3-venv
```

You can check your version after you ran these installs by entering this:

```
python3 --version
```

If you use a newer version of Ubuntu (or another Linux distribution), it
might be, that you already have Python 3.6.x or newer. If this is the case,
then you must skip Step 2b and directly jump to Step 3.

### Step 2b: Install Python 3.6

As Python 3.6 is not officially supported in Ubuntu 16.04 LTS, you need to
first install the old version as described in Step 2a. After that, you install
the inofficial backport of Python 3.6.

```
add-apt-repository ppa:jonathonf/python-3.6
apt-get update
apt-get install python3.6
update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.5 1
update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 2
python3 --version
```

The output in the terminal should show something like `Python 3.6.3` (or
newer). If it does not and you experience trouble while trying to install
Python 3.6, please have a look at
[Ubuntuhandbook.org](http://ubuntuhandbook.org/index.php/2017/07/install-python-3-6-1-in-ubuntu-16-04-lts/)
to learn more or google
[ubuntu 16.04 python 3.6](https://www.google.com/search?q=ubuntu+16.04+python+3.6&ie=utf-8&oe=utf-8).

Continue with:

```
apt-get install python3.6-venv
```

### Step 3: Installing and running the server

You should switch to a suitable directory, e.g. `/opt` before you execute the
following commands in one terminal window. Take care, that you do not close
the terminal while executing the commands, because the exported environment
variables need to be valid.

The following sequence assumes, you want to use `/opt` as a base and that you
are running within an Docker container.

```
cd /opt
export LC_ALL=C.UTF-8
export LANG=C.UTF-8
git clone https://github.com/sy2002/HWD-Perceptron.git
cd HWD-Perceptron
python3 -m venv .
source bin/activate
./install.sh --host=0.0.0.0
```

If you are not running inside Docker, replace the last line by:

```
./install.sh
```

If you want to run the server at a later moment in time, then you do not need
to install or train the server again. Instead, you can execute this:

```
cd /opt/HWD-Perceptron
export LC_ALL=C.UTF-8
export LANG=C.UTF-8
./run_server --host=0.0.0.0
```

If you are not running inside Docker, then the last line should look like this:

```
./run_server
```
