from flask import Blueprint, render_template

# Define the main blueprint
main_bp = Blueprint('main_bp', __name__)

# Root route
@main_bp.route('/')
def index():
    return render_template('index.html')

# About route
@main_bp.route('/about')
def about():
    return render_template('about.html')

# Products route
@main_bp.route('/products')
def products():
    return render_template('products.html')

# Adoptions route
@main_bp.route('/adoptions')
def adoptions():
    return render_template('adoptions.html')

# Help page route
@main_bp.route('/help_page')
def help_page():
    return render_template('help.html')
