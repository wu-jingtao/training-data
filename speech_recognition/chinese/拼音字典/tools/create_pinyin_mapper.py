import json


mapper = {"count": 0}

with open('speech_recognition/chinese/拼音字典/phonetic.txt') as f:
    for line in f:
        line = line.strip()
        for intonation in range(1, 5):
            pinyin = line + str(intonation)
            mapper[mapper["count"]] = pinyin
            mapper[pinyin] = mapper["count"]
            mapper["count"] += 1

with open('speech_recognition/chinese/拼音字典/pinyin_mapper.json', 'w') as f:
    json.dump(mapper, f)
