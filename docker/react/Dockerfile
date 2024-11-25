# 1. 使用するベースイメージを指定（Node.jsの公式イメージを使用）
FROM node:22

# 2. アプリケーションの作業ディレクトリを指定
WORKDIR /app

# 3. プロジェクトの依存関係をインストールするために package.json と package-lock.json をコピー
COPY react/webui/package.json react/webui/package-lock.json ./

# 4. 依存関係をインストール
RUN npm install

# 5. アプリケーションの全てのファイルをコンテナ内の作業ディレクトリにコピー
COPY react .

WORKDIR /app/webui

# 6. Reactアプリケーションをビルド
RUN npm run build

# 7. アプリケーションを公開するポートを指定
EXPOSE 3000

# 8. React アプリケーションを起動
CMD ["npm", "start"]