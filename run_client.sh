#!/usr/bin/env bash

cd client

case "$OSTYPE" in
  darwin*)  open nn.html ;; 
  linux*)   xdg-open nn.html ;;
  cygwin*)  cmd /c start nn.html ;;
  *)        echo "Please open client/nn.html in your web-browser." ;;
esac
