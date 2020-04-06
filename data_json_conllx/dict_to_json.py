#!/usr/bin/env python

import json
import os
import shutil
import pathlib


def make_dir():
    dirs = ['./data/line', './data/domain', './data/error', './data/final']
    for i in dirs:
        if not os.path.exists(i):
            os.makedirs(i)
    file = r'./ucloud_configure.json'
    shutil.copy(os.path.join(file), './data/final')


def turn(file_prefix):
    base_name, _ = os.path.splitext(file_prefix)

    with open('./data/raw/{}'.format(file_prefix), 'r') as load_f:
        load_dict = json.load(load_f)
        with open('./data/line/{}.json'.format(base_name), 'w', encoding='utf-8') as f:
            for i in load_dict:
                json.dump(i, f, ensure_ascii=False)
                f.write('\n')


if __name__ == "__main__":

    make_dir()

    input_file_list = [i.name for i in pathlib.Path('./data/raw').iterdir() if i.is_file()]

    for input_file in input_file_list:
        turn(input_file)



