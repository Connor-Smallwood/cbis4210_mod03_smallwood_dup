import pymysql
from flask import g

def get_db():
    if 'db' not in g:
        g.db = pymysql.connect(
            host='ixnzh1cxch6rtdrx.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
            user='syu6rdop6t3apgjp',
            password='qtt4r2qwnge2uy3e',
            db='jtrigbp7mvh4edd0',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_app(app):
    app.teardown_appcontext(close_db)
