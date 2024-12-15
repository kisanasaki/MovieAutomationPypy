# ベースイメージを指定
FROM nvidia/cuda:12.0.1-cudnn8-runtime-ubuntu20.04

# 環境変数の設定
ENV DEBIAN_FRONTEND=noninteractive \
    LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    NVIDIA_VISIBLE_DEVICES=all \
    NVIDIA_DRIVER_CAPABILITIES=all

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

# pipとサポートライブラリのアップグレード
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

# Whisperライブラリをインストール
RUN pip install --no-cache-dir git+https://github.com/openai/whisper.git

# requirements.txt をコンテナにコピー
COPY ./docker/movie/requirements.txt /app/requirements.txt
WORKDIR /app

# Python依存関係をインストール
RUN pip install --no-cache-dir -r requirements.txt

# デフォルトのコマンドを設定
CMD ["/bin/bash"]