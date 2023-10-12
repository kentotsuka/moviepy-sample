from moviepy.editor import *

# 動画の読み込み
clip = VideoFileClip('input.MP4')

# 動画の長さ
print('-----------------')
print(clip.duration)
print('-----------------')

# 音声の読み込み
audio_clip_1 = AudioFileClip('voice/Haaai.mp3')
audio_clip_2 = AudioFileClip('voice/itadakimasu.mp3')
audio_clip_3 = AudioFileClip('voice/ya.mp3')
audio_clip_4 = AudioFileClip('voice/yahoo.mp3')
audio_clip_5 = AudioFileClip('voice/yondakana?.mp3')

# 音声の連結
concat_clip = concatenate_audioclips([audio_clip_1, audio_clip_2, audio_clip_3, audio_clip_4, audio_clip_5])

# 音声の長さ
print('-----------------')
print(concat_clip.duration)
print('-----------------')

# テキストの設定
txt_clip = TextClip('Hello, World!', fontsize=100, color='white')

# テキストの表示 duration:表示する秒数、start：何秒後にスタートさせるか
txt_clip = txt_clip.set_pos('bottom').set_duration(9).set_start(1)

# ミュート
clip = clip.set_audio(None)

# 映像とテキストを重ねる
video = CompositeVideoClip([clip, txt_clip])

# 音声の追加
video = video.set_audio(concat_clip)

# 動画の作成
video.write_videofile('output.mp4')
