#!/usr/bin/env bash

echo ""
echo "sy2002's HWD Perceptron - Training and Test data installer v1.0"
echo "done on 14th of April 2018"
echo ""

if [ -f mnist_train.csv ] && [ -f mnist_test.csv ]; then
    echo "Training and test data (mnist_train.csv and mnist_test.csv) found."
    read -p "Press ENTER if you want to delete them and install new or CTRL+C to abort"
    rm mnist_train.csv mnist_test.csv
    echo ""
fi

echo "This script will download mnist_train.csv and mnist_test.csv from the"
echo "Internet so make sure you are connected and you have 130 MB of free space"
read -p "Press ENTER to continue or CTRL+C to abort"
echo ""

TRAIN_SET=https://pjreddie.com/media/files/mnist_train.csv
TEST_SET=https://pjreddie.com/media/files/mnist_test.csv

wget $TRAIN_SET || curl -O $TRAIN_SET
wget $TEST_SET || curl -O $TEST_SET

if [ ! -f mnist_train.csv ] && [ ! -f mnist_test.csv ]; then
    echo ""
    echo "========================================================================"
    echo "Something went wrong with the original server. Trying sy2002's mirror..."
    echo "========================================================================"
    echo ""

    TRAIN_SET=http://hwdp.sy2002x.de/mnist_train.csv
    TEST_SET=http://hwdp.sy2002x.de/mnist_test.csv

    wget $TRAIN_SET || curl -O $TRAIN_SET
    wget $TEST_SET || curl -O $TEST_SET
fi

echo ""

if [ -f mnist_train.csv ] && [ -f mnist_test.csv ]; then
    echo "========================================================================"

    case "$OSTYPE" in
      darwin*)  OSTP="OSX" ;; 
      linux*)   OSTP="LINUX" ;;
      bsd*)     OSTP="BSD" ;;
      *)        OSTP="unknown" ;;
    esac

    if [ $OSTP = "OSX" ] || [ $OSTP = "BSD" ]; then
        MD5_TRAIN=`md5 -q mnist_train.csv`
        MD5_TEST=`md5 -q mnist_test.csv`
    else
        MD5_TRAIN=`md5sum -b mnist_train.csv| cut -d " " -f1`
        MD5_TEST=`md5sum -b mnist_test.csv| cut -d " " -f1`
    fi

    if [ $MD5_TRAIN = "5b49cf1b57fb9d6102b559d59d99df7c" ] && [ $MD5_TEST = "c807df8d6d804ab2647fc15c3d40f543" ]; then
        echo "INSTALLATION OK"
    else
        echo "INSTALLATION MIGHT BE OK"
        echo "Download worked, but MD5 hash is wrong or could not be checked."
    fi

    echo "========================================================================"
    echo ""
else
    echo "========================================================================"
    echo "!! INSTALLATION FAILED !!"
    echo "Please consult README.md for how to install the data manually."
    echo "========================================================================"
    echo ""
fi
