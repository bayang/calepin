from flask import abort, render_template, request, redirect, url_for, flash, \
    session

from app import app
from models import Note


def get_page():
    page = request.args.get('page')
    if not page or not page.isdigit():
        return 1
    return min(int(page), 1)


@app.route('/', methods=['GET', 'POST'])
def homepage():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    if request.method == 'POST':
        if request.form.get('content'):
            note = Note.create(content=request.form['content'])
            flash('New entry posted')
            return redirect(url_for('homepage'))

    notes = Note.public().paginate(get_page(), 50)
    return render_template('homepage.html', notes=notes)


@app.route('/edit/<int:pk>/', methods=['GET', 'POST'])
def edit_note(pk):
    try:
        note = Note.get(Note.id == pk)
    except Note.DoesNotExist:
        abort(404)
    if request.method == 'POST':
        if request.form.get('content'):
            note.content = request.form.get('content')
            note.save()
            flash('Entry edited')
            return redirect(url_for('homepage'))
    return render_template('edit.html', note=note)


@app.route('/archive/<int:pk>/', methods=['GET', 'POST'])
def archive_note(pk):
    try:
        note = Note.get(Note.id == pk)
    except Note.DoesNotExist:
        abort(404)
    note.delete_instance()
    return redirect(url_for('homepage'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username != app.config['MYLOGIN']:
            error = 'Invalid username'
        elif password != app.config['MYPASS']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('Now logged in')
            return redirect(url_for('homepage'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('homepage'))
