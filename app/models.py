from . import db
from datetime import datetime 

class MovieProfile(db.Model):
    __tablename__ = 'movie_profiles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    poster = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) # Using datetime.utcnow()

    def __init__(self, title, description, poster, created_at):
        self.title = title
        self.description = description
        self.poster = poster
        self.created_at = created_at

    def __repr__(self):
        return f"Movie('{self.title}', '{self.poster}', '{self.created_at}')"
