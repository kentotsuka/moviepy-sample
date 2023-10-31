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
- `tmp/audios/`を用意し、`audio_0.mp3`のような形で`audio_`に出力させたい順に末尾に数値をつけて格納する
  - 一つ目の`audio_0.mp3`は、後述の`input.mp4`よりも短い音声にする
- `tmp/videos/`を用意し、結合したい動画を`input.mp4`という名前で格納する


## 実行

```bash
python function/by_moviepy.py
python function/by_ffmpeg.py
```