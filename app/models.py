# Add any model classes for Flask-SQLAlchemy here
from . import db
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class MovieProfile(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of MovieProfile would create a
    # Movie_profile (singular) table, but if we specify __tablename__ we can change it
    # to `Movie_profiles` (plural) or some other name.
    __tablename__ = 'movie_profiles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=False)
    poster = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    db = SQLAlchemy()
    

    def __init__(self, title, description, poster, datetime):
        self.title = title
        self.description = description
        self.poster = poster
        self.created_at = datetime

    def __repr__(self):
        return f'<MovieProfile {self.title}>'

