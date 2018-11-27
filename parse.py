# -*- coding: utf8 -*-

import json
import sys

def putpaser(filepath):
    
    with open(filepath, mode='r', encoding='utf-8') as fi:
        json_dict = json.load(fi)

    return json.dumps(json_dict, ensure_ascii=False, indent=4)

# ファイル出力する場合
# with open('parsed.json,mode='w', encoding='utf-8') as fo:
#     json.dump(json_dict, fo, ensure_ascii=False, indent=4)

# コンソール出力する場合
# print(json.dumps(json_dict, ensure_ascii=False, indent=4))

args = sys.argv

print(putpaser(args[1]))