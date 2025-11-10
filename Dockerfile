FROM python:3.10-slim-bullseye


WORKDIR /app


COPY . /app


RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    awscli ffmpeg libsm6 libxext6 unzip && \
    rm -rf /var/lib/apt/lists/*


RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 5000


CMD ["python", "app.py"]
