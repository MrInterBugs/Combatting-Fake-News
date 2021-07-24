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
nytimes = PrivateKey(publisher='NYTimes',
                     private_key='-----BEGIN EC PRIVATE KEY-----\nMHQCAQEEIG5Ygav5hReJ9WZvPJHa3r9fVyd9JxHJUi0kUu4tLvugoAcGBSuBBAAK\noUQDQgAEo7fcExc3v9kdF0lCMCMtrcIqU03AjHfu1UHNYClO3EvMF9wtKYUb1F2L\nOe4RuQaMeTxlptyDqaijN3zbJZ2S6Q==\n-----END EC PRIVATE KEY-----')
bbc = PrivateKey(publisher='BBC',
                 private_key='-----BEGIN EC PRIVATE KEY-----\nMHQCAQEEIAJNcYYp63fPZUWTy+tWosDfu8De9coRoofeeDOU2J3joAcGBSuBBAAK\noUQDQgAEp1h8PZuoY3oD83bC9I/kxj/SVfLK41e0FlX/sLM8F9/jetRTtgC4WM89\n23rJxQ9p3s79CL5+xha3oOfpriCAmA==\n-----END EC PRIVATE KEY-----')
ft = PrivateKey(publisher='Financial Times',
                private_key='-----BEGIN EC PRIVATE KEY-----\nMHQCAQEEIKtFHMrBzAhMQiNFW/kRpZVZSQGEj3QeApyU1d7Vq0k3oAcGBSuBBAAK\noUQDQgAEMwzhviezqpfVc+OBoJOlMzVkpJUrqq7TBo7+ALReehlT1s0SYKbR+Kwe\nOYUWhOpCdk9QWSdW7xxI1kBRVaiu3w==\n-----END EC PRIVATE KEY-----')
guardian = PrivateKey(publisher='Guardian',
                      private_key='-----BEGIN EC PRIVATE KEY-----\nMHQCAQEEIMMTKdk0xZXDoRVpV7y2HJz8p1syzt4IYb3EdpHA0Q5JoAcGBSuBBAAK\noUQDQgAELkQAGX3lFaxZU/2l8NdPp0GK9Cpgi5UaVYfoPEookXzgeWjVlX+tZIp8\ngqzuXERbPeX5opbXkTaQ/dvvY2UCJg==\n-----END EC PRIVATE KEY-----')
db.session.add(bbc)
db.session.add(ft)
db.session.add(guardian)
db.session.add(nytimes)
db.session.commit()
