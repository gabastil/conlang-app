from flask import render_template, redirect, url_for
from .forms import LoginForm, WordEvolutionForm
from app import app

route = app.route

pages = ['index.html',
         'login.html',
         'instructions.html',
         'word_editor.html']

data = {
    'menu' : 'Home Login Documentation Editor'.split(),
    'pages' : pages,
}

@route('/index')
@route('/')
def index():
    return render_template(pages[0], **data)

@route('/login/')
def login():
    return render_template(pages[1])

@route('/instructions/')
def instructions():
    return render_template(pages[2])

@route('/editor', methods=['GET', 'POST'])
def editor():
    form = WordEvolutionForm()
    if form.validate_on_submit():
        return 'Success'
    return render_template(pages[3])
