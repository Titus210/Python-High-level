from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4

db = SQLAlchemy()

# Creating a function to generate a UUID and return its hexadecimal representation
def generate_uuid():
    return str(uuid4())

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.String(32), primary_key=True, unique=True, default=generate_uuid)
    email = db.Column(db.String(345), unique=True)
    password = db.Column(db.Text, nullable=False)
