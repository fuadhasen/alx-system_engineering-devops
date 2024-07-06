#!/bin/bash
#scriopt to  cURL body size of url
curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}'

