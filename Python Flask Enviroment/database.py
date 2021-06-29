from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/Student/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class PrivateKey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    publisher = db.Column(db.String(80), unique=True, nullable=False)
    private_key = db.Column(db.String(2100), unique=True, nullable=False)

    def __repr__(self):
        return self.private_key
