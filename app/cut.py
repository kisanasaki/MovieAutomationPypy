from moviepy.editor import VideoFileClip, concatenate_videoclips
from pydub import AudioSegment, silence

def detect_silence(video_path, silence_threshold=-40, min_silence_len=500):
    clip = VideoFileClip(video_path)
    audio = AudioSegment.from_file(video_path, format="mp4").set_channels(1)
    
    # 無音部分を検出
    silent_ranges = silence.detect_silence(
        audio, min_silence_len=min_silence_len, silence_thresh=silence_threshold
    )
    silent_ranges = [(start / 1000, end / 1000) for start, end in silent_ranges]

    # 無音部分を除外したクリップを作成
    non_silent_clips = []
    last_end = 0
    for start, end in silent_ranges:
        if last_end < start:
            non_silent_clips.append(clip.subclip(last_end, start))
        last_end = end
    if last_end < clip.duration:
        non_silent_clips.append(clip.subclip(last_end, clip.duration))
    
    final_clip = concatenate_videoclips(non_silent_clips)
    return final_clip

# 使用例
edited_clip = detect_silence("input_video.mp4")
edited_clip.write_videofile("output_video.mp4")