from flask import Blueprint, render_template
from app.db_connect import get_db

# Define the main blueprint
main_bp = Blueprint('main_bp', __name__)

# Existing routes (index, about, products, etc.)
@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/about')
def about():
    return render_template('about.html')

@main_bp.route('/services')
def services():
    return render_template('services.html')

@main_bp.route('/products')
def products():
    return render_template('products.html')

@main_bp.route('/adoptions')
def adoptions():
    return render_template('adoptions.html')

@main_bp.route('/help_page')
def help_page():
    return render_template('help.html')

# New route for the Pets page
@main_bp.route('/pets')
def pets():
    try:
        db = get_db()
        cursor = db.cursor()

        # Query the pets table to fetch all pets
        cursor.execute('SELECT * FROM pets')
        pets = cursor.fetchall()

        return render_template('pets.html', pets=pets)
    except Exception as e:
        print(f"Database error: {e}")
        return "Error loading pets data"
