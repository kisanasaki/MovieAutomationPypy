FROM nvidia/cuda:12.0.1-cudnn8-runtime-ubuntu20.04
ENV DEBIAN_FRONTEND=noninteractive

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
        && pip install pip -U

COPY requirements.txt /root/
RUN pip install git+https://github.com/openai/whisper.git
RUN pip install -r /root/requirements.txt
