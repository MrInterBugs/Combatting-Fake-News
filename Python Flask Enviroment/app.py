"""Used to verify the authenticity of provided news to a source."""
import json

from urllib.error import HTTPError
from urllib.request import urlopen

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.serialization import load_pem_private_key

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/interbugs/keytool/database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class PrivateKey(db.Model):
    """This is the table which contains the keys for the publishers."""
    __tablename__ = 'publishers'
    publisher = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    private_key = db.Column(db.String(2100), unique=True, nullable=False)

    def __repr__(self):
        return self.private_key


GUARDIAN_API_KEY = "e75ca83b-5396-4d64-85b5-598ba5eff24a"
NYTIMES_API_KEY = "PLhsHNcQaagOwo1u6wp4f6KwgYeOlA4E"


@app.route('/')
def encrypted():
    """Returns the a json of the article and the included signature."""
    try:
        article = request.args.get('article')

        if 'https://www.theonion.com/' in article:
            return {'Parody': True,
                    'Publisher': 'Onion',
                    'Article': article}

        if 'https://www.theguardian.com/' in article:
            response = urlopen('https://content.guardianapis.com/' + (
                article.split(".com/", 1)[1]) + '?api-key=' + GUARDIAN_API_KEY)

            json_obj = json.loads(response.read().decode('utf-8'))
            private_key = read_key("Guardian")
            signature = sign_news(private_key, bytes(response))

            return {'Signature': signature.hex(),
                    'Publisher': 'Guardian',
                    'Article': json_obj}

        if 'https://www.nytimes.com/' in article:
            response = urlopen('https://api.nytimes.com/svc/mostpopular/v2/emailed/7.json?api-key=' + NYTIMES_API_KEY)

            json_obj = json.loads(response.read().decode('utf-8'))
            top20 = json_obj['results']

            for each in top20:
                if each['url'] == article:
                    private_key = read_key("NYTimes")
                    signature = sign_news(private_key, bytes(article.encode('utf-8')))

                    return {'Signature': signature.hex(),
                            'Publisher': 'NYTimes',
                            'URL': article}
            else:
                return {'Status': 'Trusted Source, Not Verifiable'}
        else:
            return {'Status': 'Untrusted Source.'}
    except HTTPError:
        return {'Status': 'Something went wrong.'}


@app.route('/publickey')
def public():
    try:
        publisher = request.args.get('publisher')
        private_key = read_key(publisher)
        return private_key.public_key().public_bytes(serialization.Encoding.DER, serialization.PublicFormat.SubjectPublicKeyInfo)
    except HTTPError:
        return {'Status': 'Something went wrong.'}


def sign_news(private_key, full_article):
    """Returns the signature of ECDSA signing the news article and other information together."""
    return private_key.sign(full_article,
                            ec.ECDSA(hashes.SHA256())
                            )


def read_key(publisher):
    """Used to read the private keys from the database."""
    private_key = str(PrivateKey.query.filter_by(publisher=publisher).first()).encode()
    return load_pem_private_key(private_key, None, default_backend())


if __name__ == '__main__':
    app.run(ssl_context=('cert.pem', 'key.pem'))
