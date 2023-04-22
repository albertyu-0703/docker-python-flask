# 使用官方 Ubuntu 22.04 image 作為基礎
FROM ubuntu:22.04

# 設置維護者資訊
LABEL maintainer="me@albert-yu.com"

# 更新套件並安裝所需套件
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python3.10 \
    python3-pip \
    python3-venv \
    && rm -rf /var/lib/apt/lists/*

# 設置工作目錄
WORKDIR /app

# 建立 Python 虛擬環境
RUN python3 -m venv venv

# 啟用虛擬環境
ENV VIRTUAL_ENV=/app/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# 複製需求檔案到工作目錄
COPY requirements.txt .

# 安裝 Python 套件
RUN pip3 install --no-cache-dir -r requirements.txt

# 複製應用程式到工作目錄
COPY . .

# 暴露 Flask 運行的埠
EXPOSE 5000

# 啟動應用程式
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
