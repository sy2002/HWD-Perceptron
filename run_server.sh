#!/usr/bin/env bash

echo ""
echo "Hint: Open an additional terminal window while this window keeps running"
echo "      and execute ./run_client.sh to access the server via your web browser."
echo ""

cd server
FLASK_APP=hwdr_server.py flask run $1
