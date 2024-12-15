# ベースイメージを指定（Python 3.9-slimを使用）
FROM python:3.9-slim

# 作業ディレクトリを設定
WORKDIR /app

# 必要なシステムパッケージをインストール
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# requirements.txtをコンテナにコピー
COPY ./docker/webapi/requirements.txt .

# Python依存関係をインストール
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# アプリケーションコードをコンテナにコピー
COPY ./webapi .

# デフォルトで実行されるコマンドを設定
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
