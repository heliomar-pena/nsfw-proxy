FROM python:3.12-bookworm

RUN mkdir -p /home/app

COPY . /home/app

ARG INSTALL_BONK="false"

RUN echo "$INSTALL_BONK";

WORKDIR /home/app/tools

# Installing rust. Needed for installing mitmproxy as python dependency
RUN apt update -y
RUN apt install make curl git build-essential scdoc -y
RUN curl --proto '=https' -tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

# Installing CLI AI Classifier tools dependencies
RUN if [ "$INSTALL_BONK" = "true" ] ; then \
        git clone https://git.sr.ht/~jamesponddotco/bonk && cd /home/app/tools/bonk && make && make install; \
    fi

WORKDIR /home/app

RUN pip install -r requirements.txt --break-system-packages

# Installing dependencies
ENTRYPOINT [ "mitmdump", "-s", "nsfw.py", "--set", "command=bonk <dir>", "--set", "level=0.2", "--listen-port", "8080" ]
