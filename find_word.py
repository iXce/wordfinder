#!/usr/bin/env python

import sys

chars = [c for c in sys.argv[1]]
chars.sort()

def gen(chars, n):
    chars_u = set(chars)
    for c in chars_u:
        if n == 1:
            yield c
        else:
            chars2 = list(chars)
            chars2.remove(c)
            for w in gen(chars2, n - 1):
                yield c + w

for w in gen(chars, int(sys.argv[2])):
    print w
