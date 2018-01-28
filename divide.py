#!/usr/bin/env python
# -*- coding:utf-8 -*-

import MeCab

text = "日本語の自然言語処理は本当にしんどい。"
tagger = MeCab.Tagger("-Owakati")
result = tagger.parse(text)
print(result)
