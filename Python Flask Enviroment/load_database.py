"""Used to populate the database as and when needed."""
from app import db, PrivateKey

db.create_all()
bbc = PrivateKey(publisher = 'BBC', private_key = '-----BEGIN EC PRIVATE KEY-----\nMHQCAQEEIAJNcYYp63fPZUWTy+tWosDfu8De9coRoofeeDOU2J3joAcGBSuBBAAK\noUQDQgAEp1h8PZuoY3oD83bC9I/kxj/SVfLK41e0FlX/sLM8F9/jetRTtgC4WM89\n23rJxQ9p3s79CL5+xha3oOfpriCAmA==\n-----END EC PRIVATE KEY-----')
ft = PrivateKey(publisher = 'Financial Times', private_key = '-----BEGIN EC PRIVATE KEY-----\nMHQCAQEEIKtFHMrBzAhMQiNFW/kRpZVZSQGEj3QeApyU1d7Vq0k3oAcGBSuBBAAK\noUQDQgAEMwzhviezqpfVc+OBoJOlMzVkpJUrqq7TBo7+ALReehlT1s0SYKbR+Kwe\nOYUWhOpCdk9QWSdW7xxI1kBRVaiu3w==\n-----END EC PRIVATE KEY-----')
guardian = PrivateKey(publisher = 'Guardian', private_key = '-----BEGIN EC PRIVATE KEY-----\nMHQCAQEEIMMTKdk0xZXDoRVpV7y2HJz8p1syzt4IYb3EdpHA0Q5JoAcGBSuBBAAK\noUQDQgAELkQAGX3lFaxZU/2l8NdPp0GK9Cpgi5UaVYfoPEookXzgeWjVlX+tZIp8\ngqzuXERbPeX5opbXkTaQ/dvvY2UCJg==\n-----END EC PRIVATE KEY-----')
db.session.add(bbc)
db.session.add(ft)
db.session.add(guardian)
db.session.commit()
