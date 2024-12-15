import whisper

def transcribe_audio(video_path):
    model = whisper.load_model("large-v3-turbo")
    result = model.transcribe(video_path)
    return result["segments"]

# 使用例
segments = transcribe_audio("./content/movie/test_ALTERED.mp4")
for segment in segments:
    print(f"{segment['start']} - {segment['end']}: {segment['text']}")