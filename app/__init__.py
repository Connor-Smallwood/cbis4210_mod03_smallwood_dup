from flask import Flask
from app.db_connect import init_app
from app.blueprints.pets import pets_bp  # Import the pets blueprint
from app.routes import main_bp  # Assuming your main routes are in app.routes
from app.blueprints.services import services_bp

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
    app.register_blueprint(pets_bp)  # Register the pets blueprint

    # Define the root route
    @app.route('/')
    def index():
        return render_template('index.html')

    return app