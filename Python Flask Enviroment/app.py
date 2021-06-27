import base64

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes
from flask import Flask
from cryptography.hazmat.primitives.asymmetric import rsa, padding

app = Flask(__name__)

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

articleTitle = b"BREAKING NEWS: Royal Holloway is a University"
articleContent = b"This is a test message to see if it works with Flask."
articleAuthor = b"Aedan Lawrence"

fullArticle = articleTitle + articleContent + articleAuthor

sig = private_key.sign(fullArticle,
                       padding.PSS(
                           mgf=padding.MGF1(hashes.SHA256()),
                           salt_length=padding.PSS.MAX_LENGTH
                       ),
                       hashes.SHA256())


@app.route('/')
def encrypted():
    return{'Signature': sig.hex(),
           'articleContent': articleContent.decode("utf-8"),
           'articleAuthor': articleAuthor.decode("utf-8"),
           'articleTitle': articleTitle.decode("utf-8")}


@app.route('/verify')
def decrypted():
    try:
        public_key = private_key.public_key()
        public_key.verify(
            sig,
            fullArticle,
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
