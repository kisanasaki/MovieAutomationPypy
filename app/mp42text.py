import whisper
from whisper.utils import get_writer
# ファイルパス
video_path = "./content/movie/test_ALTERED.mp4"
audio_path = "./content/movie"

# モデル指定
model = "large-v3-turbo"
# モデルのロード
model = whisper.load_model(model)

# 文字起こし
segments = model.transcribe(video_path, language='japanese', verbose=True,word_timestamps=True)

# srt字幕ファイル出力
writer = get_writer("txt", "./content/telop")
writer(segments, "./telop.txt")
