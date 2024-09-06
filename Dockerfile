FROM python:3.12-bookworm AS nsfw_proxy

RUN mkdir -p /home/app

COPY . /home/app

WORKDIR /home/app

# Installing rust. Needed for installing mitmproxy as python dependency
RUN apt update -y
RUN apt install make curl git build-essential scdoc -y
RUN curl --proto '=https' -tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

RUN python -m venv nsfw_proxy
RUN nsfw_proxy/bin/pip install -r requirements.txt

EXPOSE 8080
VOLUME /root/.mitmproxy

ENTRYPOINT [ "./nsfw_proxy/bin/mitmdump", "-s", "nsfw.py", "--listen-port", "8080" ]

FROM nsfw_proxy AS nsfw_proxy_bonk

RUN git clone https://git.sr.ht/~jamesponddotco/bonk && cd /home/app/bonk && make && make install;

WORKDIR /home/app

ENTRYPOINT [ "./nsfw_proxy/bin/mitmdump", "-s", "nsfw.py", "--set", "command=bonk <dir>", "--set", "level=0.2", "--listen-port", "8080" ]
