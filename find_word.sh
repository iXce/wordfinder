#!/bin/sh

python2 find_word.py $1 $2 > /tmp/possibs
grep -Fx -f fr_dic /tmp/possibs
