from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from authors_app.extensions import db
from datetime import datetime
from authors_app.extensions import db



class Book (db.Model):
    __tablename__ = "books"
    id =  db.Column(db.Integer, primary_key= True)
    title = db.Column(db.String(100), nullable=False)
    pages = db.Column(db.Integer,nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(100))
    image = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey("Users.id"))
    company_id = db.Column(db.Integer, db.ForeignKey("companies.id"))
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())
    
    
    def __init__(self, title, description, pages, users_id, price, user_id, image=None):
        self.users_id = users_id
        self.pages = pages
        self.title = title
        self.description = description
        self.users_id = users_id
        self.price = price
        self.image = image
        