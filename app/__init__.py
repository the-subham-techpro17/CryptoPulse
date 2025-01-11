from flask import Flask

def create_app():
    app = Flask(__name__)

    # Directly configuring the app here instead of using config.py
    app.config['SECRET_KEY'] = 'your-secret-key'  # Replace with your own secret key

    # Import the routes after the app is created to avoid circular imports
    from app.routes import main
    app.register_blueprint(main)

    return app
