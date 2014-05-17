#!/usr/bin/env python

locale = "fr"

import sys
import marisa_trie

trie = marisa_trie.Trie()
trie.load(locale + "_trie")

chars = list(unicode(sys.argv[1]))
chars.sort()

def gen(prefix, chars, n):
    chars_u = set(chars)
    for c in chars_u:
        subprefix = prefix + c
        if n == 1:
            if subprefix in trie:
                yield subprefix
        elif trie.has_keys_with_prefix(subprefix):
            chars2 = list(chars)
            chars2.remove(c)
            for w in gen(subprefix, chars2, n - 1):
                yield w

for w in gen("", chars, int(sys.argv[2])):
    print(w)
