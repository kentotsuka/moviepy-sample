# moviepy-sample


## バージョン
- Python 3.9.x
- MoviePy 1.0.3


## セットアップ

### MoviePyの準備
- requirements.txt を使って moviepy をインストール
```bash
pip install -r requirements.txt
```

### FFmpegのダウンロード
- pipではインストールできないので、[FFmpeg公式ダウンロードページ](https://www.ffmpeg.org/download.html)からダウンロードする


### 音声・動画の準備
- `tmp/` に合成に必要な動画音声を以下のような構成で準備する
  - 一つ目の音声 `audio_0.mp3` は、`input.mp4` よりも短い音声にする

```bash
$ tree tmp/

tmp/
├── audios
│   ├── audio_0.mp3
│   ├── audio_1.mp3
│   ├── audio_2.mp3
│   ├── audio_3.mp3
│   └── audio_4.mp3
└── videos
    └── input.mp4
```

## 実行

```bash
python function/by_moviepy.py
python function/by_ffmpeg.py
```