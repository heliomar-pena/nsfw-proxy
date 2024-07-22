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

> [!NOTE] https://docs.mitmproxy.org/stable/concepts-certificates/

1. Start mitmproxy
2. Go to mitm.it, then download the certificates and follow the instructions for your device
3. Check if connection works with pages like https://www.github.com or https://google.com.
4. You should enable the proxy on your device or browser, by example I added it on firefox.
