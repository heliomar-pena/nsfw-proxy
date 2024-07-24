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

### Installing dependencies

#### Mitm Proxy

mitmproxy is a free and open source interactive HTTPS proxy. In this project it is used for intercept, inspect, modify and replay web traffic such as HTTP/1, HTTP/2, WebSockets, or any other SSL/TLS-protected protocols. With the intention of analyze if a resource (image, gif, video, streaming) contain undesearable content, then blocking it according to your configuration.

You can download it here: https://mitmproxy.org/

#### Command Line AI Classifier

This project allow you to decide which AI tool to use for classify your content. The one I personally use by its speed and low cost on memory is BONK, and it is the only one supported currently by the project. If you know one that you want to be supported on the project please leave it as an issue and I will check it.

Here are classified the **supported** CLI AI Classifier tools. They have a tag called Installing Difficulty what will indicate if you need or not technical knowledge to install it:

- **HARD**: You will need to know about git and the programming language that it is developed. Probably will be different to install it on windows, linux or mac.
- **MEDIUM**: To install it you will need to read a documentation and follow different steps for your operative system.
- **EASY**: You only download it and click continue, continue, accept, continue, finish. (Or install it in your dependency manager if you're on linux)

|Name|Website|Installing difficulty|Language|
|----|-------|---------------------|--------|
|Bonk|[Here](https://sr.ht/~jamesponddotco/bonk/)|Hard|Rust|

#### Cloning the project

For cloning the project only run this command or download it as zip [here](https://github.com/heliomar-pena/nsfw-proxy/archive/refs/heads/dev.zip).

```sh
git clone https://github.com/heliomar-pena/nsfw-proxy.git
```

The dependencies on the requirements.txt file are only for development, since you will run this project with mitmproxy which has its own python version installed and already have mitmproxy as a dependency, so don't worry for that file for now.

### How to run the project

To run it, you need to open the file using [mitmdump](https://mitmproxy.org/#mitmdump), which allow us to interact with the HTTP requests using python.

At the moment of run mitmdump, you need to make a call to this file and also declare the arguments that will decide the behaviour of the proxy. Here is a basic example:

```sh
mitmdump -s ./nsfw.py --set command="bonk <dir>" --set level=0.1
```

And here is are we doing splitted for explanation:

- `mitmdump`: Calling mitmdump command which starts an HTTP proxy server and allow us to use a python script to interact with him.
- `-s`: Short way to say script, allow insert a script as option
- `./nsfw.py`: The path to the `nsfw.py` file that you cloned from this repo
- `--set`: Allow you insert arguments that will be used for the script.
- `command="bonk <dir>"`: First argument for the script, which says to the script what command to use. The `<dir>` is a reserved key that will be replaced on the program for the path of the image, so the CLI Tool can use this path to get the image and analyze it.
- `--set`: Allow you to insert another argument to the script.
- `level=0.1`: NSFW Classifiers Tools as Bonk gives you a **level** of NSFW that can have an image. Here you can configure what is the min level for you to considerate an image NSFW.

#### Personalizing behavior of the script

As you can see above, you need to run the command:

```sh
mitmdump -s ./nsfw.py
```

Then you can modify the behaviour of the script using `--set` to insert arguments and so define which CLI tool to use for analyzing images, what level of NSFW would you like to allow, etc...

In this section you will see all the commands that you can pass to `--set` and its allowed values.

|Name|Optional|Default value|Value Type|Example values|Note|
|----|--------|-------------|----------|--------------|----|
|command|:white_check_mark:|""|str|`bonk <dir>`|It should include `<dir>` which is the slot where the script will include the image's path|
|level|:white_check_mark:|0.3|float|0.1|You can use a float or an integer: 0.1, 0.2, 1, 3|

#### Installing certificates

> [!NOTE]
> https://docs.mitmproxy.org/stable/concepts-certificates/
> Mitmproxy can decrypt encrypted traffic on the fly, as long as the client trusts mitmproxy’s built-in certificate authority. Usually this means that the mitmproxy CA certificate has to be installed on the client device.

Before start navigating using our proxy we need to install the certificates. At this moment, if you try to connect to the proxy and then navigate on the web probably you'll found a message rejecting the conection and some warnings, this is because your browser or your computer doesn't trust in the proxy and needs the certificates to trust in him.

As we are using a mitmproxy proxy, we will install its certificates. To do this, you will need to follow the next steps:

1. Start the project as explained above
2. Go to [mitm.it](mitm.it), then download the certificates and follow the instructions for your device or browser.
3. Check if connection works with pages like https://www.github.com or https://google.com.

### Connecting to the proxy

This will vary depending of if you wants to install it on an Operative System as Android, iOs, Linux, Windows, Mac or on a browser like Safari, Firefox, Chrome, etc...

In all cases, you will need the proxy URL, which by default is `localhost:8080`, where `8080` is the port where the proxy is running on your network. If you want change the port you can use the option `--listen-port`, by example `mitmdump -s ./nsfw.py --listen-port 8081`.

Then, you can follow the instructions on the web for the system you have:

- [Windows](https://support.microsoft.com/en-us/windows/use-a-proxy-server-in-windows-03096c53-0554-4ffe-b6ab-8b1deee8dae1)
- [Firefox](https://support.mozilla.org/en-US/kb/connection-settings-firefox)
- [Chrome](https://oxylabs.io/resources/integrations/chrome)
- [Android](https://proxyway.com/guides/android-proxy-settings)
- [iOS](https://help.getfoxyproxy.org/index.php/knowledge-base/how-to-use-proxy-services-with-iphoneipadios/)
- [Debian](https://computingforgeeks.com/how-to-set-system-proxy-on-debian-linux/)
- [Fedora](https://computingforgeeks.com/configure-system-wide-proxy-settings-on-centos-rhel-fedora/)
- [Arch](https://wiki.archlinux.org/title/Proxy_server)

If your system doesn't appear here just search it is just that there is too many variety of systems and versions to include all of them here. You can search your specific case in Google and I am sure you will found the solution.
