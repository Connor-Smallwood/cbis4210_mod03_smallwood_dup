from flask import Blueprint, render_template
from app.db_connect import get_db

# Blueprint for services
services_bp = Blueprint('services_bp', __name__)

@services_bp.route('/services')
def services():
    try:
        db = get_db()
        cursor = db.cursor()

        # Execute a query to get services data
        cursor.execute('SELECT * FROM services')
        services = cursor.fetchall()

        return render_template('services.html', services=services)
    except Exception as e:
        print(f"Database connection error: {e}")
        return "Error connecting to the database"
