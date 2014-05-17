#!/usr/bin/env python

locale = "fr"

from unidecode import unidecode
import marisa_trie

dic = [unidecode(unicode(l.strip(), "utf8")) for l in open(locale + "_dic")]
trie = marisa_trie.Trie(dic)
trie.save(locale + "_trie")
