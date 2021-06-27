from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes
from flask import Flask
from cryptography.hazmat.primitives.asymmetric import rsa, padding

app = Flask(__name__)

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)
private_key2 = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

article = b"This is a test message to see if it works with Flask."
article2 = b"This is a test message to see if it works with Flask."

sig = private_key.sign(article,
                       padding.PSS(
                           mgf=padding.MGF1(hashes.SHA256()),
                           salt_length=padding.PSS.MAX_LENGTH
                       ),
                       hashes.SHA256())

sig2 = private_key2.sign(article2,
                         padding.PSS(
                             mgf=padding.MGF1(hashes.SHA256()),
                             salt_length=padding.PSS.MAX_LENGTH
                         ),
                         hashes.SHA256())


@app.route('/')
def encrypted():
    return sig


@app.route('/verify')
def decrypted():
    try:
        public_key = private_key.public_key()
        public_key.verify(
            sig,
            article,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return "Valid"
    except InvalidSignature:
        return "Invalid"


if __name__ == '__main__':
    app.run()
