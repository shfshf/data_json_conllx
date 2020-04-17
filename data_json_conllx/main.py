#!/usr/bin/env python

import os
import pathlib

from tokenizer_tools.conllz.writer import write_conllx
from data_json_conllx.utils import remove_files_in_dir

from data_json_conllx.processor import process_one_line, CheckFailedError


def make_dir():
    dirs = ['./data/final', './data/domain', './data/error']
    for i in dirs:
        if not os.path.exists(i):
            os.makedirs(i)


def main(file_prefix):
    base_name, _ = os.path.splitext(file_prefix)

    log_file = './data/error/{}.error'.format(base_name)

    with open('./data/raw/{}'.format(file_prefix)) as fd, open(log_file, 'wt') as logger:
        output_lines = []
        seq_list = []
        for raw_line in fd:
            line = raw_line.strip()
            if not line:
                continue

            try:
                seq, sentence = process_one_line(line, logger)
            except CheckFailedError as e:
                continue
            else:
                seq_list.append(seq)
                output_lines.append(sentence)

        # write_conll(output_lines, 'data/{}.text'.format(file_prefix))
        with open('./data/domain/{}.conllx'.format(base_name), 'wt') as output_fd:
            write_conllx(output_lines, output_fd)


if __name__ == "__main__":

    make_dir()
    # remove_files_in_dir('./data/error')
    # remove_files_in_dir('./data/domain')
    input_file_list = [i.name for i in pathlib.Path('./data/raw').iterdir() if i.is_file()]

    for input_file in input_file_list:
        main(input_file)






