#!/bin/bash

PID=$(ps aux | grep $1 | grep python)

if [ -z "$PID" ]; then
  /usr/bin/python $1 &
else
  echo "$1 active!!"
fi;

exit 0
