from moviepy.editor import *
import config
import boto3
import os

PROFILE_NAME = config.PROFILE_NAME
BUCKET_NAME = config.BUCKET_NAME

# s3へアクセス
session = boto3.Session(profile_name = PROFILE_NAME)
s3 = session.resource('s3')
bucket = s3.Bucket(BUCKET_NAME)

# s3から動画をダウンロード
bucket.download_file('original_videos/input.MP4', 'tmp_videos/input.mp4')
print('-----------------')
print('S3から動画のダウンロード完了')
print('-----------------')

# 動画の読み込み
clip = VideoFileClip('tmp_videos/input.mp4')

# 動画の長さ
print('-----------------')
print('動画の長さ(秒)')
print(clip.duration)
print('-----------------')

# 音声の読み込み
audio_clip_1 = AudioFileClip('audio/Haaai.mp3')
audio_clip_2 = AudioFileClip('audio/itadakimasu.mp3')
audio_clip_3 = AudioFileClip('audio/ya.mp3')
audio_clip_4 = AudioFileClip('audio/yahoo.mp3')
audio_clip_5 = AudioFileClip('audio/yondakana?.mp3')

# 音声の連結
concat_clip = concatenate_audioclips([audio_clip_1, audio_clip_2, audio_clip_3, audio_clip_4, audio_clip_5])

# 音声の長さ
print('-----------------')
print('音声の長さ(秒)')
print(concat_clip.duration)
print('-----------------')

# 音声の追加
video = clip.set_audio(concat_clip)

# 動画の作成
video.write_videofile('tmp_videos/output.mp4')

# S3へアップロード
bucket.upload_file('tmp_videos/output.mp4', 'videos/output.mp4')
print('-----------------')
print('S3へのアップロード完了')
print('-----------------')

# 動画の削除
os.remove('tmp_videos/input.mp4')
os.remove('tmp_videos/output.mp4')
print('-----------------')
print('不要なファイルを削除しました。')
print('-----------------')