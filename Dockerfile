FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive


RUN apt-get update && \
    apt-get install -y python3 wget git curl && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app


COPY . .

RUN chmod +x ./mixer.sh

EXPOSE 8080

CMD ["python3", "app.py"]
