"""Defines the constraints of the database"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/Student/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class PrivateKey(db.Model):
    """This is the table which contains the keys for the publishers."""
    __tablename__ = 'publisher'
    publisher = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    private_key = db.Column(db.String(2100), unique=True, nullable=False)

    def __repr__(self):
        return self.private_key


class NewsArticle(db.Model):
    """This is the table which contains different news articles"""
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True)
    publisher = db.Column(db.String(80), ForeignKey('publisher.publisher'))
    author = db.Column(db.String(80), unique=False, nullable=False)
    title = db.Column(db.String(250), unique=False, nullable=False)
    content = db.Column(db.String(5000), unique=False, nullable=False)

    def __repr__(self):
        return {'Publisher': self.publisher, 'Title': self.title, 'Author': self.author, 'Content': self.content}
