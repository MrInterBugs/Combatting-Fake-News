from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from flask import Flask
from cryptography.hazmat.primitives.asymmetric import padding

app = Flask(__name__)

with open("test.pem", 'rb') as pem_in:
    pemlines = pem_in.read()
private_key = load_pem_private_key(pemlines, None, default_backend())

articleTitle = "BREAKING NEWS: Royal Holloway is a University"
articleContent = "This is a test message to see if it works with Flask."
articleAuthor = "Aedan Lawrence"

fullArticle = str.encode(articleTitle) + str.encode(articleContent) + str.encode(articleAuthor)

sig = private_key.sign(fullArticle,
                       padding.PSS(
                           mgf=padding.MGF1(hashes.SHA256()),
                           salt_length=padding.PSS.MAX_LENGTH
                       ),
                       hashes.SHA256())


@app.route('/')
def encrypted():
    return{'Signature': sig.hex(),
           'articleContent': articleContent,
           'articleAuthor': articleAuthor,
           'articleTitle': articleTitle}


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
