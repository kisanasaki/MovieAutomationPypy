import whisper
from moviepy.editor import VideoFileClip

input_video_path = "test_ALTERED.mp4"
output_exo_path = "output.exo"
def transcribe_audio(video_path):
    """
    Whisperで動画から音声を文字起こしする。

    :param video_path: 動画ファイルのパス
    :return: 文字起こし結果（リスト形式）
    """
    print("Whisperで文字起こし中...")
    model = whisper.load_model("base")
    result = model.transcribe(video_path)
    segments = result["segments"]
    print("文字起こし完了!")
    return segments


def generate_exo_from_transcription(transcription, video_path, output_exo_path):
    """
    文字起こし結果を元にEXOファイルを生成する。

    :param transcription: 文字起こし結果（リスト形式）
    :param video_path: 動画ファイルのパス
    :param output_exo_path: 出力するEXOファイルのパス
    """
    # 動画の長さを取得
    video = VideoFileClip(video_path)
    video_duration = int(video.duration * 1000)  # ミリ秒に変換

    # EXOヘッダー
    exo_content = f"""[exedit]
width=1920
height=1080
rate=30
scale=1
length={video_duration // (1000 // 30)}
audio_rate=44100
audio_ch=2
"""

    # 各セグメントをEXO形式に追加
    for i, segment in enumerate(transcription, start=1):
        start_time = int(segment["start"] * 1000)  # 秒をミリ秒に変換
        end_time = int(segment["end"] * 1000)
        text = segment["text"]

        # EXOオブジェクト定義
        exo_content += f"""
[{i}]
start={start_time}
end={end_time}
layer=1
group=1
overlay=1
camera=0

[{i}.0]
_name=テキスト
サイズ=48
表示速度=100.0
移動速度=100.0
文字列={text}
"""

    # EXOファイルの出力
    with open(output_exo_path, "w", encoding="utf-8") as exo_file:
        exo_file.write(exo_content)
    print(f"EXOファイルを生成しました: {output_exo_path}")


if __name__ == "__main__":
    # 入力ファイルと出力パスを指定
    input_video_path = "example.mp4"
    output_exo_path = "output.exo"

    # Whisperで文字起こし
    transcription = transcribe_audio(input_video_path)

    # EXOファイルを生成
    generate_exo_from_transcription(transcription, input_video_path, output_exo_path)
