# han2kip
han2kip is a package for converting Taiwanese Hokkien Hanzi (HAN) to its phonetic representation, Kàu-io̍k-pōo Tâi-lô (KIP).

## Installing
```
$ pip install han2kip
```

## Usage
```python
from han2kip import kip_converter

# HAN sentence
sentence = '今仔日天氣真好'
print(kip_converter.translate(sentence))
"kin-á-ji̍t thinn-khì tsin-hó"

sentence = ['今仔日天氣真好，小明！', '風真透~', '愛你一世人']
print(kip_converter.translate(sentence))
"['kin-á-ji̍t thinn-khì tsin-hó，sió-bîng！', 'hong tsin-thàu~', 'ài lí tsi̍t-sì-lâng']"
```