#!/bin/bash

echo 'ジェットカットします'

auto-editor ./content/movie/test.mp4

echo '文字起こし&SRT字幕ファイルを生成します'

python3 mp42text.py
