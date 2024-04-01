import jieba
import json
import re
import os


current_file_path = os.path.realpath(__file__)
base_path = '\\'.join(current_file_path.split('\\')[:-1]) + '\\data\\'
han2kip = json.load(open(base_path + 'words.json', 'r', encoding='utf-8'))
jieba.load_userdict(base_path + 'dict.txt')
punctuation = re.compile(r'[\u0021-\u002F\u003A-\u0040\u005B-\u0060\u007B-\u007E\u3000-\u303F\uFF01-\uFF5E]+')


def translate(sentence):
    if isinstance(sentence, str):
        line = []
        for word in jieba.cut(sentence, cut_all=False):
            if word in han2kip:
                line.append(han2kip[word])
            else:
                line.append(translate_separately(word).lower().replace(' ', '-'))
        ret = ' '.join(line)
        ret = re.sub(rf' *({punctuation.pattern}) *', r'\1', ret)
        return ret
    elif isinstance(sentence, list) or isinstance(sentence, tuple):
        ret_list = []
        for sen in sentence:
            line = []
            for word in jieba.cut(sen, cut_all=False):
                if word in han2kip:
                    line.append(han2kip[word])
                else:
                    line.append(translate_separately(word).lower().replace(' ', '-'))
            ret = ' '.join(line)
            ret = re.sub(rf' *({punctuation.pattern}) *', r'\1', ret)
            ret_list.append(ret)
        return ret_list


def translate_separately(sentence):
    ret = []
    i = 0
    to_add = ''
    double_dict = {'啊': '--ah', '矣': '--ah', '啦': '--lah', '無': '--bô', '喏': '--noh', '的': '--ê', '咧': '--leh'}
    if sentence[-1] in double_dict:
        to_add = double_dict[sentence[-1]]
        sentence = sentence[:-1]
    while i < len(sentence):
        for j in range(len(sentence) - i, 0, -1):
            if sentence[i:i + j] in han2kip:
                ret.append(han2kip[sentence[i:i + j]])
                i += j
                break
            if j == 1:
                ret.append(sentence[i:i + j])
                i += j
    return ' '.join(ret) + to_add