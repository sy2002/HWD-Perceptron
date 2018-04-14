#!/usr/bin/env bash

echo ""
echo "Handwritten Digits Recognizer via Perceptron Network - INSTALLER v1.0"
echo "done by sy2002 at 14th of April 2018"
echo ""
echo "You might want to run this inside a virtual environment, so that we"
echo "don't mess with your python setup by installing these requirements:"
echo ""
cat requirements.txt
echo ""
read -p "Press ENTER to continue or CTRL+C to abort"

py_chk=`python --version|cut -d " " -f2|cut -d "." -f1`
if [ ! $py_chk = "3" ]; then
    echo "Python 3 is needed for this project."
    exit 1
fi

pip_chk=`pip --version|cut -d " " -f1`
pip_version_chk=`pip --version|cut -d " " -f6|cut -d "." -f1`
if [ ! $pip_chk = "pip" ] || [ ! $pip_version_chk = "3" ]; then
    echo "pip for Python 3 is needed for this project."
    exit 1
fi

echo ""
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
./run_server.sh
