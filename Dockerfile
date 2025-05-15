FROM python:3.10.16-slim AS base

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY config_files/requirements.txt .

COPY config_files/announcements_files/ /app/config_files/announcements_files/

RUN pip install -r requirements.txt

COPY /src /app/src

COPY .env /app

CMD ["uvicorn", "src.RatPartyMixAPI:app", "--host", "0.0.0.0", "--port", "8888"]