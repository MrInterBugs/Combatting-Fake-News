"""Used to verify the authenticity of provided news to a source."""
import base64
import json
import ssl

from urllib.error import HTTPError
from urllib.request import urlopen
from urllib.parse import urlparse

import requests as requests
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.serialization import load_pem_private_key

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/interbugs/keytool/database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Keys(db.Model):
    """This is the table which contains the keys for the publishers."""
    __tablename__ = 'publishers'
    publisher = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    public_key = db.Column(db.String(2100), unique=True, nullable=False)

    def __repr__(self):
        return self.public_key


GUARDIAN_API_KEY = "e75ca83b-5396-4d64-85b5-598ba5eff24a"
NYTIMES_API_KEY = "PLhsHNcQaagOwo1u6wp4f6KwgYeOlA4E"

PRIVATE_KEY = load_pem_private_key("-----BEGIN EC PRIVATE "
                                   "KEY-----\nMHcCAQEEIObwTwlLFrqf8XTXQAT90AZ7WfrgCa5l7A0U286T63CkoAoGCCqGSM49"
                                   "\nAwEHoUQDQgAELDIqPmr5Oxklns5GgKTLrxfS0WcKIjaCCW2ZsjBpwxcnQAItqUKS"
                                   "\nh5GCfj0tW6jVm4adiCCAKIDOBWhvIYqZ1Q==\n-----END EC PRIVATE KEY-----".encode(),
                                   None, default_backend())


@app.route('/')
def encrypted():
    """Returns the a json of the article and the included signature."""
    try:
        article = request.args.get('article')

        if 'https://www.theguardian.com/' in article:
            response = urlopen('https://content.guardianapis.com/' + (
                article.split(".com/", 1)[1]) + '?api-key=' + GUARDIAN_API_KEY)

            json_obj = json.loads(response.read().decode('utf-8'))

            if json_obj['response']['status'] == 'ok':
                signature = sign_news(PRIVATE_KEY, bytes(article.encode('utf-8')))
                return {'Signature': (base64.b64encode(signature)).decode('ascii'),
                        'Publisher': 'Guardian',
                        'URL': article}
            else:
                return {'Status': 'Untrusted Source.'}

        if 'https://www.nytimes.com/' in article:
            response = urlopen('https://api.nytimes.com/svc/mostpopular/v2/emailed/7.json?api-key=' + NYTIMES_API_KEY)

            json_obj = json.loads(response.read().decode('utf-8'))
            top20 = json_obj['results']

            for each in top20:
                if each['url'] == article:
                    signature = sign_news(PRIVATE_KEY, bytes(article.encode('utf-8')))
                    return {'Signature': (base64.b64encode(signature)).decode('ascii'),
                            'Publisher': 'NYTimes',
                            'URL': article}
            else:
                return {'Status': 'Trusted Source, Not Verifiable'}

        if 'https://www.theonion.com/' in article:
            return {'Satire': True,
                    'Publisher': 'Onion',
                    'Article': article}

        else:
            return check_other(article)
    except HTTPError:
        return {'Status': 'Something went wrong.'}


def sign_news(private_key, full_article):
    """Returns the signature of ECDSA signing the news article and other information together."""
    return private_key.sign(full_article,
                            ec.ECDSA(hashes.SHA256())
                            )


def read_key(publisher):
    """Used to read the private keys from the database."""
    return str(Keys.query.filter_by(publisher=publisher).first())


def check_other(article):
    parsed = urlparse(article).netloc
    cert = ssl.get_server_certificate((parsed, 443))
    if cert == read_key(parsed):
        response = requests.get(article)
        if response.ok:
            signature = sign_news(PRIVATE_KEY, bytes(article.encode('utf-8')))
            return {'Signature': (base64.b64encode(signature)).decode('ascii'),
                    'Publisher': parsed,
                    'URL': article}
        return {'Status': 'Possible Trusted Source, Not Verifiable'}
    else:
        return {'Status': 'Untrusted Source.'}


if __name__ == '__main__':
    app.run(ssl_context=('cert.pem', 'key.pem'))
