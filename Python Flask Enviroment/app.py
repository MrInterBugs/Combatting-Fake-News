"""Used to verify the authenticity of provided news to a source."""
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_pem_private_key

from flask import Flask, request
from database import PrivateKey

app = Flask(__name__)


@app.route('/')
def encrypted():
    """Returns the a json of the article and the included signature."""
    article = request.args.get('article')
    print(article)
    return {'Signature': SIGNATURE.hex(),
            'articleContent': ARTICLE_CONTENT,
            'articleAuthor': ARTICLE_AUTHOR,
            'articleTitle': ARTICLE_TITLE,
            'articlePublisher': ARTICLE_PUBLISHER}


@app.route('/verify')
def decrypted():
    """Quick example to make sure the the signature matches."""
    try:
        public_key = PRIVATE_KEY.public_key()
        public_key.verify(
            SIGNATURE,
            FULL_ARTICLE,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return "Valid"
    except InvalidSignature:
        return "Invalid"


def sign_news(private_key, full_article):
    """Returns the signature of RSA signing the news article and other information together."""
    return private_key.sign(full_article,
                            padding.PSS(
                                mgf=padding.MGF1(hashes.SHA256()),
                                salt_length=padding.PSS.MAX_LENGTH
                            ),
                            hashes.SHA256())


def read_key(publisher):
    """Used to read the private keys from the database."""
    private_key = str(PrivateKey.query.filter_by(publisher=publisher).first()).encode()
    return load_pem_private_key(private_key, None, default_backend())


ARTICLE_TITLE = "BREAKING NEWS: Royal Holloway is a University"
ARTICLE_CONTENT = "This is a test message to see if it works with Flask."
ARTICLE_AUTHOR = "Aedan Lawrence"
ARTICLE_PUBLISHER = "Financial Times"

FULL_ARTICLE = str.encode(ARTICLE_TITLE) + str.encode(ARTICLE_CONTENT) + str.encode(ARTICLE_AUTHOR)
PRIVATE_KEY = read_key(ARTICLE_PUBLISHER)
SIGNATURE = sign_news(PRIVATE_KEY, FULL_ARTICLE)

if __name__ == '__main__':
    app.run()
