# 概要
これは動画編集の一部を自動化するツールです。具体的には、全体の工程（1～8）のうち3～5を自動化することを目的としています。

1. 企画
    1.1. 動画のテーマを決める
    1.2. 動画の構成を決める
2. 撮影
3. 編集
    3.1. ジャンプカット
    3.2. テロップ
    3.3. 効果音自動挿入　←ｲﾏｺｺ
4. 動画の確認 

# テストデータ

# 参考
https://blog.k-bushi.com/post/tech/ai/extract-text-from-video-or-audio-with-whisper/
https://engineering.monstar-lab.com/jp/post/2023/12/08/Subtitling-with-Whisper/

# コマンド
docker comopse up -d
docker exec -it automation-movie-1 bash
