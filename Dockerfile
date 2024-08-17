FROM python:3.12-bookworm

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

ENTRYPOINT [ "mitmdump", "--listen-port", "8080" ]
