#!/usr/bin/env python

import os
import pathlib

from tokenizer_tools.conllz.iterator_reader import conllx_iterator_reader
from tokenizer_tools.conllz.writer import write_conllx

current_dir = os.path.dirname(os.path.abspath(__file__))

input_file_list = [str(i) for i in pathlib.Path('./data/domain').iterdir() if i.is_file()]

data = list(conllx_iterator_reader(input_file_list))

with open('./data/all_data.conllx', 'wt') as fd:
    write_conllx(data, fd)
