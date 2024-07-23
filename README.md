# NSFW Proxy

Script in python that can be used for creating a self-hosted proxy for NOT SAFE FOR WORK content filtering.

## Features

### AI Images Classification

- Block images in all sites using AI for classification.
- Custom AI CLI Tool can be passed as argument to use it.
- Disable AI detection if you want.

### Programmatic Images Classification

- Blacklist with more than 28000 NSFW websites.
- All resources in blacklists websites are blocked (Video, images and gifs), no is needed analyze them.

## Roadmap features

- [ ] Buffering Video NSFW classification.
- [ ] Streaming video NSFW classification.
- [ ] Websockets NSFW classification.
- [ ] NSFW Text classification.
- [ ] Adding WhiteList in case someone doesn't wanted filter content on certain page.
- [ ] Adding compatibility with more classification NSFW tools

### Unconfirmed features Roadmap

- [ ] Web user interface for configuration once service is started instead of only command line interface.
- [ ] User interface for start, stop and configure the service.

### Roadmap chores

- [ ] Improve installation documentation.
- [ ] Adding **How to** configure it on a router / modem for all users in a same network. (This will work for public networks which wanted filter this content and for entire families).
- [ ] Adding **How to** configure it on a VPS for using out of the house. (In case someone doesn't wanted use it only locally but also when he is out).

## How to install?

### Mitm Proxy

mitmproxy is a free and open source interactive HTTPS proxy. In this project it is used for intercept, inspect, modify and replay web traffic such as HTTP/1, HTTP/2, WebSockets, or any other SSL/TLS-protected protocols. With the intention of analyze if a resource (image, gif, video, streaming) contain undesearable content, then blocking it according to your configuration.

You can download it here: https://mitmproxy.org/

### Command Line AI Classifier

This project allow you decide which AI tool to use for classify your content. The one I personally use by its speed and low cost on memory is BONK, and it is the only one supported currently by the project. If you know one that you want to be supported on the project please leave it as an issue and I will check it.

Here are classified the **supported** CLI AI Classifier tools. They have a tag called Installing Difficulty what will indicate if you need or not technical knowledge to install it:

- **HARD**: You will need to know about git and the programming language that it is developed. Probably will be different to install it on windows, linux or mac.
- **MEDIUM**: To install it you will need to read a documentation and follow different steps for your operative system.
- **EASY**: You only download it and click continue, continue, accept, continue, finish. (Or install it in your dependency manager if you're on linux)

|Name|Website|Installing difficulty|Language|
|----|-------|---------------------|--------|
|Bonk|[Here](https://sr.ht/~jamesponddotco/bonk/)|Hard|Rust|

> ![NOTE] https://docs.mitmproxy.org/stable/concepts-certificates/

1. Start mitmproxy
2. Go to mitm.it, then download the certificates and follow the instructions for your device
3. Check if connection works with pages like https://www.github.com or https://google.com.
4. You should enable the proxy on your device or browser, by example I added it on firefox.
