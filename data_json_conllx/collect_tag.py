#!/usr/bin/env python

from tokenizer_tools.tagset.offset.corpus import Corpus


corpus = Corpus.read_from_file("data/all_data.conllx")

with open("data/final/entity.txt", "wt") as fd:
    fd.write("\n".join(corpus.annotation_tags()))
