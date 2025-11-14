from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f'<User {self.username}>'
    
class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)

    buy_price = db.Column(db.Numeric(10,2), nullable=False)
    rent_price = db.Column(db.Numeric(10,2), nullable=False)

    is_available = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<Book {self.title} by {self.author}>'
    
#Orders
#   id
#   user_id
#   order_date
#   total_amount -> how much the entire order cost
#   payment_status -> if the payment has been made or not

#Order Items
#   id
#   order_id
#   book_id
#   type -> buy/rent
#   item_price
#   rent_due_date -> Only needed for rentals

#Managers
#   user_id
#   user_name