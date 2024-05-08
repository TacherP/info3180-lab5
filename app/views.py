import os
from app import app, db
from flask import render_template, request, send_file, flash, jsonify, redirect, url_for,send_from_directory
from app.models import MovieProfile
from app.forms import MovieForm 
from werkzeug.utils import secure_filename
from flask_wtf.csrf import generate_csrf
from datetime import datetime

# Routing for your application

# Root route
@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")

# Endpoint to get CSRF token
@app.route('/api/v1/csrf-token', methods=['GET'])
def get_csrf():
    return jsonify({'csrf_token': generate_csrf()})

# Endpoint to save a new movie
@app.route('/api/v1/movies', methods=['POST'])
def movies():
    form = MovieForm()
    if request.method == 'POST' and form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        poster = form.poster.data
        created_at = datetime.datetime.now()
        filename = secure_filename(poster.filename)
        poster.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        new_movie = MovieProfile(title, description, filename, created_at)
        db.session.add(new_movie)
        db.session.commit()
        return jsonify(message='Movie added successfully', status='success', title=title, description=description, poster=filename)
    return jsonify(errors=form_errors(form))

# Endpoint to get all movies
@app.route('/api/v1/movies', methods=['GET'])
def get_movies():
    movies = MovieProfile.query.all()
    movie_list = []
    for movie in movies:
        poster_url = url_for('get_movie_poster', filename=movie.poster, _external=True)
        movie_list.append({
            'id': movie.id,
            'title': movie.title,
            'description': movie.description,
            'poster': poster_url
        })
    return jsonify(movies=movie_list)


# Endpoint to serve movie posters
@app.route('/api/v1/posters/<filename>', methods=['GET'])
def get_poster(filename):
    return send_from_directory(os.path.join(os.getcwd()), filename)

# Helper function to collect form errors
def form_errors(form):
    error_messages = []
    for field, errors in form.errors.items():
        for error in errors:
            message = f"Error in the {getattr(form, field).label.text} field - {error}"
            error_messages.append(message)
    return error_messages

# Function to send a static text file
@app.route('/<file_name>.txt')
def send_text_file(file_name):
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)

# Function to add headers to responses
@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

# Custom 404 page
@app.errorhandler(404)
def page_not_found(error):
    return jsonify(message="Page not found"), 404
