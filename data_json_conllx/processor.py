#!/usr/bin/env python

import sys
import json
# Warning: Do not install the “bson” package from pypi.
# PyMongo comes with its own bson package;
# doing “pip install bson” or “easy_install bson” installs a third-party package that is incompatible with PyMongo.
# pip install pymongo

from bson import json_util as bson


from tokenizer_tools.tagset.offset.sequence import Sequence
from tokenizer_tools.conllz.sentence import SentenceX
from tokenizer_tools.tagset.converter.offset_to_biluo import offset_to_biluo
from tokenizer_tools.tagset.offset.exceptions import OffsetSpanCheckError
from tokenizer_tools.tagset.offset.span import Span


# process json one line
def process_one_line(line, logger=sys.stderr):
    obj = bson.loads(line)
    # print(obj)
    text = obj['text']
    intent = obj['intent']
    id = obj["id"]
    seq = Sequence(text, label=intent, id=id)
    for entity in obj['entities']:
        start = int(entity['start'])  # original index start at 0
        end = int(entity['end'])
        entity = entity['entity']

        try:
            span = Span(start, end, entity)  # may raise OffsetSpanCheckError
        except OffsetSpanCheckError as e:
            logger.write("{}\tspan init failed: {}\n".format(id, e))
            raise CheckFailedError

        # get value which is not in corpus_item object
        # span.fill_text(corpus_item['text'])

        seq.span_set.append(span)

    encoding = offset_to_biluo(seq)  # may raise AssertionError
    # print(encoding)

    sentence = SentenceX(word_lines=text, attribute_lines=[encoding], id=seq.id)
    sentence.meta = {'label': intent}

    return seq, sentence


class CheckFailedError(Exception):
    pass


if __name__ == "__main__":

    test_input = """{"id": "5d11c0344420bb1e20078fd9", "entities": [{"end": 2, "entity": "地点", "length": 2, "start": 0, "value": "上海"}, {"end": 5, "entity": "日期", "length": 2, "start": 3, "value": "明天"}], "text": "上海的明天的天气", "intent": "查询天气", "domain": "weather"}"""


    seq, seqence = process_one_line(test_input)

    print(seq)

    # Sequence(text=['上', '海', '的', '明', '天', '的', '天', '气'], span_set=SpanSet(
    #          [Span(0, 2, '地点', value=['上', '海'], normal_value=None), Span(3, 5, '日期', value=['明', '天'], normal_value=None)]),
    #          id='5d11c0344420bb1e20078fd9', label='查询天气', extra_attr={})