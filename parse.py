# -*- coding: utf8 -*-

import json

with open('blacklist.json', mode='r', encoding='utf-8') as fi:
    json_dict = json.load(fi)

# ファイル出力する場合
with open('parsed.json',mode='w', encoding='utf-8') as fo:
    json.dump(json_dict, fo, ensure_ascii=False, indent=4)

# コンソール出力する場合
print(json.dumps(json_dict, ensure_ascii=False, indent=4))
