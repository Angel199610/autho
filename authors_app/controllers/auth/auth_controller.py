from flask import Blueprint, request, json, jsonify
from authors_app.models.users import User


# 'auth' is my blue print, (api/v1/auth)  is the general naming convesion for APIs
auth = Blueprint('auth', __name__, url_prefix='api/v1/auth')


# we decorate the path using the blueprint which is auth
@auth.route('/register', methods=['POST'])
def register():# creating a function 
    first_name =  request.json['first_name'] #storing the incoming requests
    last_name =  request.json['last_name']
    email = request.json['email']
    password = request.json['password']
    contact = request.json['contact']
    # user_type = request.json['user_type']
    biography = request.json['biography']
    image = request.json['image']
    
    
    #validation and constraints(more like returning a responses in json type in form a dictionary)
    #first format
    if not first_name:
        return jsonify({"error":'Your first name is required'})
    
    if not last_name:
        return jsonify({"error":'Your last name is required'})
    
    if not first_name: 
        return jsonify({"error":'Your first name is required'})
    
    if not email:
        return jsonify({"error":'Your email is required'})
    
    if not password:
        return jsonify({"error":'Your password is required'})
    
    if not contact:
        return jsonify({"error":'Your contact is required'})
    
    # if not user_type:
    #     return jsonify({"error":'Your user type is required'})
    
    if not image:
        return jsonify({"error":'Your image is required'})
    
    # if user_type == 'author' and not biography:
    #     return jsonify({"error":'Your biography is required'})
    
    if len(password)<6: # checking the length of the password
        return jsonify({"error":'Your password is must contain 6 characters'})
    
    #creating a query for email and contact cause they are unique to return a reponse
    if User.query.filter_by(email=email).first():
        return jsonify({"error": 'Your email already exist'})
    
    if User.query.filter_by(contact=contact).first():
        return jsonify({"error": 'Your contact already exist'})
    
   
    
    
    
    
    
    
    #Second format
    # if not first_name or not last_name