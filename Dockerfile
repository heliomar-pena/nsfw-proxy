FROM python:3.12-bookworm AS nsfw_proxy

RUN mkdir -p /home/app

COPY . /home/app

WORKDIR /home/app

# Installing rust. Needed for installing mitmproxy as python dependency
RUN apt update -y
RUN apt install make curl git build-essential scdoc -y
RUN curl --proto '=https' -tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

RUN pip install -r requirements.txt --break-system-packages

EXPOSE 8080
VOLUME /root/.mitmproxy

ENTRYPOINT [ "mitmdump", "-s", "nsfw.py", "--listen-port", "8080" ]

FROM nsfw_proxy AS nsfw_proxy_bonk

RUN git clone https://git.sr.ht/~jamesponddotco/bonk && cd /home/app/bonk && make && make install;

WORKDIR /home/app

RUN pip install -r requirements.txt --break-system-packages

ENTRYPOINT [ "mitmdump", "-s", "nsfw.py", "--set", "command=bonk <dir>", "--set", "level=0.2", "--listen-port", "8080" ]
