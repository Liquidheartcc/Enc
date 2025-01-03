FROM python:3.10.12-slim-bullseye

# Setup home directory, non interactive shell and timezone
RUN mkdir /bot /tgenc && chmod 777 /bot
WORKDIR /bot
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Africa/Lagos
ENV TERM=xterm

# Install Dependencies
RUN apt-get update && apt-get upgrade -y
RUN apt-get install git aria2 bash wget curl pv jq python3-pip mkvtoolnix mediainfo handbrake-cli psmisc -y && python3 -m pip install --upgrade pip setuptools

# Install latest ffmpeg
COPY --from=mwader/static-ffmpeg:7.0.1 /ffmpeg /bin/ffmpeg
COPY --from=mwader/static-ffmpeg:7.0.1 /ffprobe /bin/ffprobe

# Copy files from repo to home directory
COPY . .

# Install python3 requirements
RUN pip3 install -r requirements.txt
RUN playwright install
RUN playwright install-deps

# Start bot
CMD ["bash","run.sh"]
