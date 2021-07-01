"""Used to populate the database as and when needed."""
from database import db, PrivateKey, NewsArticle

db.create_all()
bbc = PrivateKey(publisher = 'BBC', private_key = '-----BEGIN EC PRIVATE KEY-----\nMHQCAQEEIAJNcYYp63fPZUWTy+tWosDfu8De9coRoofeeDOU2J3joAcGBSuBBAAK\noUQDQgAEp1h8PZuoY3oD83bC9I/kxj/SVfLK41e0FlX/sLM8F9/jetRTtgC4WM89\n23rJxQ9p3s79CL5+xha3oOfpriCAmA==\n-----END EC PRIVATE KEY-----')
ft = PrivateKey(publisher = 'Financial Times', private_key = '-----BEGIN EC PRIVATE KEY-----\nMHQCAQEEIKtFHMrBzAhMQiNFW/kRpZVZSQGEj3QeApyU1d7Vq0k3oAcGBSuBBAAK\noUQDQgAEMwzhviezqpfVc+OBoJOlMzVkpJUrqq7TBo7+ALReehlT1s0SYKbR+Kwe\nOYUWhOpCdk9QWSdW7xxI1kBRVaiu3w==\n-----END EC PRIVATE KEY-----')
db.session.add(bbc)
db.session.add(ft)
article1 = NewsArticle(publisher = 'BBC', author = 'Aedan Lawrence', title = 'BREAKING NEWS: Royal Holloway is a University', content = 'This is a test message to see if it works with Flask.')
article2 = NewsArticle(publisher = 'Financial Times', author = 'Aedan Lawrence', title = 'BREAKING NEWS: I live in Sussex', content = 'This is a test message to see if it works with Flask.')
db.session.add(article1)
db.session.add(article2)
db.session.commit()
