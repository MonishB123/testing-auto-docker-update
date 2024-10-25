FROM python:3.9-slim

WORKDIR /app

COPY main.py .

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN apt-get install gcc g++ -y

COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt

CMD ["python3", "main.py"]