#!/bin/bash

echo "Enter yout git comment followed [ENTER]: "

read COMMENT

if [ -z "$COMMENT" ]; then
   echo "Comment cannot be empty"
else
   git add -A && git commit -m "$COMMENT" && git  push origin master
   echo "git commit done!"
fi;

exit 0
