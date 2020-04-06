#!/usr/bin/env python


from data_json_conllx.processor import process_one_line


def test_process_one_line():

    test_input = """{"id": "5d11c0344420bb1e20078fd9", "entities": [{"end": 2, "entity": "地点", "length": 2, "start": 0, "value": "上海"}, {"end": 5, "entity": "日期", "length": 2, "start": 3, "value": "明天"}], "text": "上海的明天的天气", "intent": "查询天气", "domain": "weather"}"""

    seq, seqence = process_one_line(test_input)

    gold_seq = "Sequence(text=['上', '海', '的', '明', '天', '的', '天', '气'], span_set=SpanSet([Span(0, 2, '地点', value=['上', '海'], normal_value=None), Span(3, 5, '日期', value=['明', '天'], normal_value=None)]), id='5d11c0344420bb1e20078fd9', label='查询天气', extra_attr={})"
    assert str(seq) == gold_seq
