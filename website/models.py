from . import db
from flask_login import UserMixin
from datetime import datetime ,timezone
from werkzeug.security import check_password_hash ,generate_password_hash

class Customer(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(100),unique=True)
    username = db.Column(db.String(100),unique=True)
    password_hash = db.Column(db.String(150))
    date_join = db.Column(db.DateTime(),default=datetime.now(timezone.utc))

    @property
    def password(self):
        raise AttributeError("Password is not a readable Attribute")
    
    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password=password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password=password)
    
    def __str__(self):
        return f"<Customer {self.id}>"  