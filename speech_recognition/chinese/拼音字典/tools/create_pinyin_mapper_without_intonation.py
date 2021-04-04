import json


mapper = {"count": 0}

with open('speech_recognition/chinese/拼音字典/phonetic.txt') as f:
    for i, pinyin in enumerate(f):
        pinyin = pinyin.strip()
        mapper[i] = pinyin
        mapper[pinyin] = i
        mapper["count"] += 1

with open('speech_recognition/chinese/拼音字典/pinyin_mapper_without_intonation.json', 'w') as f:
    json.dump(mapper, f)
