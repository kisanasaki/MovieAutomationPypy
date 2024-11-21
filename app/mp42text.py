import whisper
from whisper.utils import get_writer
# ファイルパス
transcribe_path = "./content/movie/test_ALTERED.mp4"
# モデルのロード
model = whisper.load_model("large-v3-turbo")

# 文字起こし
result = model.transcribe(transcribe_path, language='japanese', verbose=True,word_timestamps=True)

# srt字幕ファイル出力
writer = get_writer("srt", "./content/telop")
writer(result, "./telop.srt")
