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

## Install using docker

Install it using docker is the easier way to have it running on your computer if you're not familiarized with python. You will found the [docker repository here](https://hub.docker.com/r/heliomarpena/nsfw_proxy/tags), you can access and select the tag you think better fits your needs.

I prepared two types of tags for you, one of them runs nsfw_proxy without CLI Classifier Image, the other one runs the proxy with BONK ans CLI Classifier Image.

I will be creating more images for more CLI Classifier tools when they were supported.

Here is how to run the last version of NSFW Proxy with and without bonks.

### Run it first time (pull the image, create a container, configure ports and volumes if needed)

This is how you could do for run the image the first time. This will create a container with a configuration that you can reuse each time you want to run the container, so you probably will use this only the first time.

#### Run it with image classifier

```sh
mkdir -p mitmproxy-certificates && docker run -p 13000:8080 --name nsfw_proxy_bonk -v `pwd`/mitmproxy-certificates:/root/.mitmproxy heliomarpena/nsfw_proxy:latest-bonk
```

#### Run it without image classifier

```sh
mkdir -p mitmproxy-certificates && docker run -p 13000:8080 --name nsfw_proxy -v `pwd`/mitmproxy-certificates:/root/.mitmproxy heliomarpena/nsfw_proxy:latest
```

#### Explanation

What the above commands does is:

- `mkdir mitmproxy-certificates`: Creates a new folder called mitmproxy-certificates.
- `docker run`: Pull an image from dockerhub, creates a new container using that image and then run it with the provided configuration.
  - `heliomarpena/nsfw_proxy:latest`: Run the docker repository heliomarpena/nsfw_proxy:latest (or latest-bonk depending which one you choose)
  - `-p 13000:8080`: Bind the port 13000 of your computer with the port 8080 of the container, so you can use the port 13000 to connect to the proxy that is exposed on the port 8080 of the container.
  - ```-v `pwd`/mitmproxy-certificates:/root/.mitmproxy```: Creates a volume on the folder `mitmproxy-certificates` for the folder `/root/.mitmproxy` of the container. This will save the mitmproxy certificates between versions, so you don't need reinstall them each time you deletes your container and creates a new one.
  - `--name nsfw_proxy`: Adds a name to the container for easy future references.

### Run it normally

Once you have already pulled, configured and created a new container you can run it normally. If you added a name to your containers you would be able to run them using:

```sh
docker start nsfw_proxy
```

or

```sh
docker start nsfw_proxy_bonk
```

Respectively to the version you decided to install.

And that's all! If you already have your container running you can go directly to [Connecting to the proxy](#connecting-to-the-proxy) section, where you will connect to the container and use it as a proxy for filtering NSFW content from your network.

## Install using Python 3.12

### Dependencies

The dependencies you'll need are only Python 3.12 or bigger and any CLI AI Classifier Tool from the [list of supported cli classifiers](./docs/supported_cli_classifiers.md).

| Name               | Website                                                        | Optional | Description                                                                                                                                           |
| ------------------ | -------------------------------------------------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Python             | [Here](https://www.python.org/downloads/release/python-3120/)  | **No**   | Used for install mitmproxy and the script you'll be running in this project is written in Python                                                      |
| Classifier AI Tool | [See supported list here](./docs/supported_cli_classifiers.md) | **YES**  | Used for classifying all images no matter its origin. E.g if you are on instagram and appears a NSFW image it will be catched by the classifier tool. |

### Cloning the project and installing Python's dependencies

For cloning the project only run this command or download it as zip [here](https://github.com/heliomar-pena/nsfw-proxy/archive/refs/heads/dev.zip).

```sh
git clone https://github.com/heliomar-pena/nsfw-proxy.git
```

### Installation

Once cloned the repository, you can install the dependencies on the `requirements.txt` file. For this you can follow any guide on internet [like this](https://www.freecodecamp.org/news/python-requirementstxt-explained#how-to-work-with-a-requirements-txt-file) or try with the next command:

```sh
pip install -r requirements.txt
```

In case you are seeing an error similar to this: 'error:externally-managed-environment', the recommended is that you install it using the [virtual env feature of python](https://docs.python.org/3/library/venv.html)

#### Install it using virtual envs

This will create an isolated space for saving the dependencies that you're installing, so avoiding breaking your system during the installation of new dependencies. You can check the [doc](https://docs.python.org/3/library/venv.html) for more information.

```sh
python3.12 -m venv nsfw_proxy
nsfw_proxy/bin/pip install -r requirements.txt
```

#### Force installation on your system (could break some of your system dependencies)

> ![WARNING]
> This method is highly unrecommended as it could break some of your system dependencies

In case you want to keep it simple you could install the dependencies directly on your system using the next command.

```sh
pip install -r requirements.txt --break-system-packages
```

### Running the project

To run it, you need to open the file using [mitmdump](https://mitmproxy.org/#mitmdump), which allow us to interact with the HTTP requests using python.

You can run it on your terminal, and it's installed during the [installing python's dependencies step](#cloning-the-project-and-installing-pythons-dependencies) when you run `pip install -r requirements.txt` command.

At the moment of run mitmdump, you need to make a call to this file and also declare the arguments that will decide the behaviour of the proxy. Here is a basic example:

```sh
mitmdump -s ./nsfw.py --set command="bonk <dir>" --set level=0.1
```

If you have installed it using virtual envs (venv), your mitmdump binary would be on the virtual env bin folder. [here](#install-it-using-virtual-envs) the virtual env was `nsfw_proxy` and the folder would be created on the same folder where you executed the command, so if you're still on that folder you just have to run:

```sh
./nsfw_proxy/bin/mitmdump -s ./nsfw.py --set command="bonk <dir>" --set level=0.1
```

And here is are we doing splitted for explanation:

- `mitmdump`: Calling mitmdump command which starts an HTTP proxy server and allow us to use a python script to interact with him.
- `-s`: Short way to say script, allow insert a script as option
- `./nsfw.py`: The path to the `nsfw.py` file that you cloned from this repo
- `--set`: Allow you insert arguments that will be used for the script.
- `command="bonk <dir>"`: First argument for the script, which says to the script what command to use. The `<dir>` is a reserved key that will be replaced on the program for the path of the image, so the CLI Tool can use this path to get the image and analyze it.
- `--set`: Allow you to insert another argument to the script.
- `level=0.1`: NSFW Classifiers Tools as Bonk gives you a **level** of NSFW that can have an image. Here you can configure what is the min level for you to considerate an image NSFW.

> ![NOTE]
> In case you installed it on a [virtual env](#install-it-using-virtual-envs), you probably should run it from your virtual env folder, if you only copied and pasted the script above, then it will be `nsfw_proxy` and will be on the same folder were you executed the command.
> For example `nsfw_proxy/bin/python mitmdump -s ./nsfw.py --set command="bonk <dir>" --set level=0.1`

#### Personalizing behavior of the script

As you can see above, you need to run the command:

```sh
mitmdump -s ./nsfw.py
```

Then you can modify the behaviour of the script using `--set` to insert arguments and so define which CLI tool to use for analyzing images, what level of NSFW would you like to allow, etc...

In this section you will see all the commands that you can pass to `--set` and its allowed values.

| Name    | Optional           | Default value | Value Type | Example values | Note                                                                                       |
| ------- | ------------------ | ------------- | ---------- | -------------- | ------------------------------------------------------------------------------------------ |
| command | :white_check_mark: | ""            | str        | `bonk <dir>`   | It should include `<dir>` which is the slot where the script will include the image's path |
| level   | :white_check_mark: | 0.3           | float      | 0.1            | You can use a float or an integer: 0.1, 0.2, 1, 3                                          |

#### Installing certificates

> [!NOTE] https://docs.mitmproxy.org/stable/concepts-certificates/
> Mitmproxy can decrypt encrypted traffic on the fly, as long as the client trusts mitmproxy’s built-in certificate authority. Usually this means that the mitmproxy CA certificate has to be installed on the client device.

Before start navigating using our proxy we need to install the certificates. At this moment, if you try to connect to the proxy and then navigate on the web probably you'll found a message rejecting the conection and some warnings, this is because your browser or your computer doesn't trust in the proxy and needs the certificates to trust in him.

As we are using a mitmproxy proxy, we will install its certificates. To do this, you will need to follow the next steps:

1. Start the project as explained above
2. Go to [mitm.it](mitm.it), then download the certificates and follow the instructions for your device or browser.
3. Check if connection works with pages like https://www.github.com or https://google.com.

## Connecting to the proxy

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
