"""Used to populate the database as and when needed."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/Student/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class PrivateKey(db.Model):
    """This is the table which contains the keys for the publishers."""
    __tablename__ = 'publishers'
    publisher = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    private_key = db.Column(db.String(2100), unique=True, nullable=False)

    def __repr__(self):
        return self.private_key


db.create_all()
server = PrivateKey(publisher='Server',
                    private_key='-----BEGIN EC PRIVATE KEY-----\nMHcCAQEEIObwTwlLFrqf8XTXQAT90AZ7WfrgCa5l7A0U286T63CkoAoGCCqGSM49\nAwEHoUQDQgAELDIqPmr5Oxklns5GgKTLrxfS0WcKIjaCCW2ZsjBpwxcnQAItqUKS\nh5GCfj0tW6jVm4adiCCAKIDOBWhvIYqZ1Q==\n-----END EC PRIVATE KEY-----')
db.session.add(server)
db.session.commit()
