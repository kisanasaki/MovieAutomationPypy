# ベースイメージを指定
FROM nvidia/cuda:12.0.1-cudnn8-runtime-ubuntu20.04

# 必要なシステムパッケージをインストール
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends \
        gcc \
        curl \
        wget \
        sudo \
        pciutils \
        python3-all-dev \
        python-is-python3 \
        python3-pip \
        git \
        ffmpeg \
        portaudio19-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# pipのアップグレード
RUN pip install --no-cache-dir --upgrade pip

# Whisperライブラリをインストール
RUN pip install --no-cache-dir git+https://github.com/openai/whisper.git

# requirements.txt をコンテナにコピー
COPY ./docker/movie/requirements.txt .

# Python依存関係をインストール
RUN pip install --no-cache-dir -r requirements.txt

# コンテナが実行されたときのデフォルトのコマンドを設定（必要に応じて追加）
CMD ["bash"]
