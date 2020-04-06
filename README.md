
## 依赖
安装 mongodb， 参考 mongodb 官方文档

### Under Ubuntu
```bash
sudo apt install mongodb-clients
```

## python 依赖
```bash
pip install -r requirements.txt
```

## 处理流程
实际处理过程如下：

* dict_to_json.py
* main.py
* merge_data.py
* split_data.py
* collect_tag.py
* collect_label.py
* write_metadata.py

直接调用 `all_in_one.sh` 就可以自动顺序执行上述处理过程。

## 输出文件
* data/final/test.conllx
* data/final/train.conllx
* data/final/entity.txt
* data/final/label.txt
* data/final/metadata.json
