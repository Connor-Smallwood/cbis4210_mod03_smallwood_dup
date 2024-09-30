from flask import Blueprint, render_template, request

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/services')
def services():
    return render_template('services.html')

@main.route('/products')
def products():
    return render_template('products.html')

@main.route('/adoptions')
def adoptions():
    return render_template('adoptions.html')

@main.route('/help')
def help_page():
    return render_template('help.html')

@main.route('/search')
def search():
    query = request.args.get('query')
    return render_template('search_results.html', query=query)
