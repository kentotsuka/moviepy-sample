"""
FFmpegとMoviePyを使った動画・音声合成
- VScode上で開くと音声が出力されないが、SlackやLINE上では音声は出力される
"""
from moviepy.editor import *
import subprocess


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

        # 結合した音声のMP3ファイルを作成
        combined_audio.write_audiofile("tmp/audios/combined_audio.mp3")

        # 動画と音声の合成するコマンド
        ffmpeg_combine_command = [
            "ffmpeg",
            "-i", "tmp/videos/input.mp4",
            "-i", "tmp/audios/combined_audio.mp3",
            "-map", "0:v",
            "-map", "1:a",
            "-c:v", "copy",
            "-c:a", "aac",
            "-strict", "experimental",
            "tmp/videos/output.mp4"
        ]

        # 動画と音声の合成
        subprocess.run(ffmpeg_combine_command, check=True)

        # サムネイルを生成するコマンド
        ffmpeg_thumbnail_command = [
            "ffmpeg",
            "-i", "tmp/videos/input.mp4",
            "-ss", "00:00:01",
            "-vframes", "1",
            "tmp/videos/thumbnail.jpg"
        ]

        # サムネイル生成
        subprocess.run(ffmpeg_thumbnail_command, check=True)

        return True

    except Exception as e:
        return False

# 実行
lambda_handler()
