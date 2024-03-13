from  flask import Flask

from flask_sqlalchemy import SQLAlchemy

from authors_app.extensions import db, migrate






# it helps us to work with mulitple instances
# For this case we create the instances within the function not using @app
def create_app():
    app = Flask(__name__)
   
    
    app.config.from_object('config.Config')
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    from authors_app.models import users
    from authors_app.models import book
    from authors_app.models import company

    
    @app.route('/')
    def home():
        return "Hello world"
    
    
    
    return app


# if __name__ == "__main__":
#     app = create_app()
#     app.run(debug=True)