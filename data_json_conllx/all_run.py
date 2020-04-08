import os
os.system("python -m data_json_conllx.dict_to_json")
os.system("python -m data_json_conllx.main")
os.system("python -m data_json_conllx.merge_data")
os.system("python -m data_json_conllx.split_data")
os.system("python -m data_json_conllx.collect_tag")
os.system("python -m data_json_conllx.collect_label")
os.system("python -m data_json_conllx.write_metadata")