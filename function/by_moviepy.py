"""
MoviePyを使った動画・音声合成
- ローカルでは動作するが、Lambda上で実行すると音声なしの動画が生成されることがある
- write_videofileでコーデックがうまく定義されないことが関係している
"""
from moviepy.editor import *


def lambda_handler():
    try:
        video_clip = VideoFileClip("tmp/videos/input.mp4")
        video_length = video_clip.duration

        # 1個目の音声の長さ > 動画の長さであれば、処理を中断
        if AudioFileClip("tmp/audios/audio_0.mp3").duration > video_length:
            raise Exception("一つ目の音声が動画の音声よりも長い")

        if not convert_video(video_clip, AudioFileClip("tmp/audios/audio_0.mp3")):
            raise Exception("動画・音声の合成で失敗")

    except Exception as e:
        print("❌ ERROR")
        print(e)
    else:
        print("✅ SUCCESS")


def convert_video(video_clip, first_audio):
    """
    動画・音声の合成
    """
    combined_audio = first_audio

    try:
        # 二個目以降の音声の結合処理
        for i in range(1, 5):
            audio_clip = AudioFileClip(f"tmp/audios/audio_{i}.mp3")

            # 音声の合計長がビデオの長さ未満である場合に新たに結合
            if (combined_audio.duration + audio_clip.duration < video_clip.duration):
                combined_audio = concatenate_audioclips([combined_audio, audio_clip])
            else:
                break

        # 動画と音声の合成する
        video_clip.set_audio(combined_audio).write_videofile("tmp/videos/output.mp4")

        return True

    except Exception as e:
        return False

# 実行
lambda_handler()
