#!/usr/bin/env bash

python -m data_json_conllx.dict_to_json
python -m data_json_conllx.main
python -m data_json_conllx.merge_data
python -m data_json_conllx.split_data
python -m data_json_conllx.collect_tag
python -m data_json_conllx.collect_label
python -m data_json_conllx.write_metadata