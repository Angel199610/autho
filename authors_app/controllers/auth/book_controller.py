from flask import Blueprint,request, jsonify
from authors_app.models.book import Book

# Blue print
book=Blueprint('book',__name__,url_prefix='api/v1/book')


# creating a end point that will help to register a new user
@book.route('/register', methods=["POST"])
def register():

    title=request.json["title"]
    last_name=request.json["last_name"]
    email=request.json["email"]
    image=request.json["image"]
    biography=request.json["biography"]
    # user_type=request.json["user_type"]
    password=request.json["password"]