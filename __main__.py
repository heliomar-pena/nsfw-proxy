from proxy import main
from nsfw_filter_plugin import NsfwFilterPlugin

if __name__ == '__main__':
    main(
        port=8081,
        cert_file="https-signed-cert.pem",
        key_file="https-key.pem",
        plugins=[NsfwFilterPlugin]
    )
