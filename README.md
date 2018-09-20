# JSONデータをインデントして出力する

入手したJSONデータがインデントされていなかった場合に、内容を整形して出力する。ちょこちょこ使いそうなので、メモ書きしておく。

なお、データはUTF-8な前提。

[参考](https://docs.python.jp/3/library/json.html#basic-usage)

## 注意事項

```python
    json.dump(json_dict, fo, ensure_ascii=False, indent=4)
```

`indent`を記述しておかないと1行で出力されちゃうので注意。

