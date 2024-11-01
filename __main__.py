from proxy import main
from nsfw_filter_plugin import NsfwFilterPlugin

if __name__ == '__main__':
    main(
        port=8081,
        ca_cert_file="certificates/domain.crt",
        ca_key_file="certificates/domain.key",
        ca_signing_key_file="certificates/domain-sign.key",
        plugins=[NsfwFilterPlugin]
    )
