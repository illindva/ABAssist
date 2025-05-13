import os
import logging
from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
from sqlalchemy.orm import DeclarativeBase
from werkzeug.middleware.proxy_fix import ProxyFix
from dotenv import load_dotenv

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Load environment variables
load_dotenv()

# Create SQLAlchemy base class
class Base(DeclarativeBase):
    pass

# Initialize extensions
db = SQLAlchemy(model_class=Base)
login_manager = LoginManager()

def create_app():
    # Create Flask app
    app = Flask(__name__)
    
    # Configure app
    app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key")
    app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)
    
    # Database configuration - SQLite by default
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///abassist.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    # Uncomment to use Azure PostgreSQL
    # app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("AZURE_POSTGRES_URI")
    
    # Uncomment to use Microsoft SQL Server
    # app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("MSSQL_URI")
    
    # Initialize database
    db.init_app(app)
    
    # Initialize login manager
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'info'
    
    # Register blueprints
    from auth import auth_bp
    app.register_blueprint(auth_bp)
    
    from app1 import app1_bp
    app.register_blueprint(app1_bp, url_prefix='/app1')
    
    from app2 import app2_bp
    app.register_blueprint(app2_bp, url_prefix='/app2')
    
    from app3 import app3_bp
    app.register_blueprint(app3_bp, url_prefix='/app3')
    
    # Home route
    @app.route('/')
    def home():
        return render_template('home.html')
    
    # Create database tables
    with app.app_context():
        db.create_all()
    
    return app
