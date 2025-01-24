from flask import Flask
from flask_cors import CORS

# Function to create and configure the app
def create_app():
    app = Flask(__name__)
    
    # Enable Cross-Origin Resource Sharing (CORS)
    CORS(app)
    
    # Register routes
    from app.routes import api
    app.register_blueprint(api)

    return app
