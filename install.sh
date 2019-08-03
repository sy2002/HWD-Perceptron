#!/usr/bin/env bash

echo ""
echo "Handwritten Digits Recognizer via Perceptron Network - INSTALLER v1.1"
echo "done by sy2002 on 22nd of April 2018"
echo ""
echo "You might want to run this inside a virtual environment, so that we"
echo "don't mess with your python setup by installing these requirements:"
echo ""
cat requirements.txt
echo ""
read -p "Press ENTER to continue or CTRL+C to abort"
echo ""

if [ ! -x "$(command -v python)" ] || [ ! -x "$(command -v pip)" ]; then
  echo "Error: python or pip is not installed."
  echo "You need Python 3 and pip for Python 3."
  echo "Please read section 'Troubleshooting' in README.md"
  echo ""
  exit 1
fi

py_chk=`python --version 2>&1|cut -d " " -f2|cut -d "." -f1`
if [ ! "$py_chk" -ge "3" ]; then
    echo "Error: Python 3 is needed for this project. It seems, that running the"
    echo "command 'python' yields to Python 2 instead of Python 3. You can check"
    echo "this by trying 'python --version'."
    echo "Please read section 'Troubleshooting' in README.md"
    echo ""
    exit 1
fi


if [ "$py_chk" -eq "3" ]; then
    py_subv=`python --version 2>&1|cut -d " " -f2|cut -d "." -f2`
    if [ ! "$py_subv" -ge "7" ]; then
        echo "Error: Python 3.7 or newer is needed for this project."
        echo ""
        exit 1
    fi
fi

if [ ! -x "$(command -v curl)" ] && [ ! -x "$(command -v wget)" ]; then
    echo "Error: curl or wget are needed to install the training data."
    echo "Install either curl or wget or install the training data manually."
    echo "Read server/training/README.md to learn more."
    echo ""
    exit 1
fi

printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' =
echo "    INSTALLING DEPENDENCIES"
printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' =
pip install -r requirements.txt

echo ""
printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' =
echo "    INSTALLING TRAINING DATA"
printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' =
cd server/training
./install_data.sh

echo ""
printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' =
echo "    ASCII ART DATA TEST"
printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' =
cd ../..
./show_data.py 3

echo ""
printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' =
echo "    TRAINING THE NETWORK"
printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' =
cd server
rm -f saved_nn/test-epoch-1.npz
python hwdt.py

echo ""
printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' =
echo "    RUNNING THE REST API SERVER"
printf '%*s\n' "${COLUMNS:-$(tput cols)}" '' | tr ' ' =
cd ..
./run_server.sh $1
