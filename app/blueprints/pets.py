from flask import Blueprint, render_template, request, redirect, url_for
from app.db_connect import get_db

# Define the blueprint for pets
pets_bp = Blueprint('pets_bp', __name__)

# Route for viewing and adding pets
@pets_bp.route('/pets', methods=['GET', 'POST'])
def pets():
    db = get_db()
    cursor = db.cursor()

    # Handle form submission to add a new pet
    if request.method == 'POST':
        # Get data from the form
        name = request.form['name']
        breed = request.form['breed']
        age = request.form['age']
        price = request.form['price']

        # Insert the new pet into the database
        try:
            cursor.execute(
                'INSERT INTO pets (name, breed, age, price) VALUES (%s, %s, %s, %s)',
                (name, breed, age, price)
            )
            db.commit()  # Commit the changes to the database
            return redirect(url_for('pets_bp.pets'))  # Redirect to the pets page after adding the pet
        except Exception as e:
            db.rollback()  # Rollback in case of error
            print(f"Error inserting pet: {e}")
            return "There was an issue adding the pet"

    # Query the pets table to fetch all pets for display
    try:
        cursor.execute('SELECT * FROM pets')
        pets = cursor.fetchall()
        print(f"Fetched {len(pets)} pets from the database.")  # Log the number of fetched pets
        return render_template('pets.html', pets=pets)
    except Exception as e:
        print(f"Error loading pets data: {e}")  # Log any error that occurs
        return "Error loading pets data"
