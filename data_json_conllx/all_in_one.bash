#!/usr/bin/env bash

python ./dict_to_json.py
python ./main.py
python ./merge_data.py
python ./split_data.py
python ./collect_tag.py
python ./collect_label.py
python ./write_metadata.py