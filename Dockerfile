# ✅ Use a newer and supported base image
FROM python:3.10-slim-bullseye

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# ✅ Update and install required system packages (awscli, ffmpeg, etc.)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    awscli ffmpeg libsm6 libxext6 unzip && \
    rm -rf /var/lib/apt/lists/*

# ✅ Install Python dependencies (from your requirements.txt)
RUN pip install --no-cache-dir -r requirements.txt

# Expose port for Flask
EXPOSE 5000

# ✅ Run your Flask app
CMD ["python", "app.py"]
