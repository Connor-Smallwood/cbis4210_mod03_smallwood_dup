from flask import Flask
from app.routes import main_bp  # Import main routes
from app.blueprints.services import services_bp  # Import services blueprint
from app.db_connect import init_app  # Correct import for db_connect

def create_app():
    app = Flask(__name__)

    # Directly setting app configuration
    app.config['DB_HOST'] = 'ixnzh1cxch6rtdrx.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
    app.config['DB_USER'] = 'syu6rdop6t3apgjp'
    app.config['DB_PASSWORD'] = 'qtt4r2qwnge2uy3e'
    app.config['DB_NAME'] = 'jtrigbp7mvh4edd0'

    # Initialize the database
    init_app(app)

    # Register the services blueprint
    app.register_blueprint(main_bp)  # Register main routes
    app.register_blueprint(services_bp)

    # Define the root route
    @app.route('/')
    def index():
        return render_template('index.html')

    return app