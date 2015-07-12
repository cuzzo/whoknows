#! /usr/bin/env python

import sys
import re

try:
    author_lines = sys.argv[1]
except:
    author_lines = sys.stdin.read().split("\n")

authors = {}
for line in author_lines:
    line = re.sub("\w+and\w+|,|\+", "&", line).split("&")
    author_names = [x.strip() for x in line]
    for author in author_names:
        if len(author) == 0:
            continue
        authors[author] = True

print("\n".join(authors.keys()))
