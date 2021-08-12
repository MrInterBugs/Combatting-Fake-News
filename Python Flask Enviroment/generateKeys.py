import ssl

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec


def save_key():
    private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
    pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption(),
    )
    with open('test.pem', 'wb') as pem_out:
        pem_out.write(pem)

    pem = private_key.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )
    with open('test_public.pem', 'wb') as pem_out:
        pem_out.write(pem)


def get_web_key(parsed):
    cert = ssl.get_server_certificate((parsed, 443))
    return cert


print(get_web_key("www.ft.com"))
print(get_web_key("www.bbc.co.uk"))
print(get_web_key("www.washingtonpost.com"))
