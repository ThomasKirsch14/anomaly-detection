# FROM arm64v8/python:3.9
FROM python:3.9-slim
WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y \
    git \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/ultralytics/yolov5.git

WORKDIR /usr/src/app/yolov5

RUN pip install --no-cache-dir -r requirements.txt

COPY yolov5/runs/train/gpu100-2/weights/best.pt /usr/src/app/yolov5/weights/best.pt

CMD ["python", "detect.py", "--weights", "weights/best.pt", "--source", "0"] 