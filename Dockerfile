#FROM ubuntu:latest
FROM python:3.10

WORKDIR /app

COPY . /app

RUN rm -rf .env


#Define environment variable to get dotenv file path
ARG ENV_FILE_PATH
COPY $ENV_FILE_PATH /app



# CRON INSTALLATION
RUN apt-get update && apt-get -y install cron
COPY config_files/cronfile /etc/cron.d/cronfile
RUN chmod 0644 /etc/cron.d/cronfile
RUN crontab /etc/cron.d/cronfile
RUN touch /var/log/cron.log
CMD cron && tail -f /var/log/cron.log

RUN chmod 0744 RatPartyMixAPI.py DailyBot.py Bot.py

# INSTALLATION OF REQUIREMENTS
RUN pip install -r config_files/requirements.txt

RUN ls -la

# ENVIRONMENT VARIABLES
ENV PORT=8888
EXPOSE 8888


CMD ["cron", "-f"]
