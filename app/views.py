from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}

    posts = [
        {
            'author':{'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author':{'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', 
        title='Home', 
        user=user,
        posts=posts)

@app.route('/grid')
def grid():
    return render_template('grid.html', title='Grid')

@app.route('/index_02_02')
def index_02_02():
    return render_template('02_02.html', title='Grid')

@app.route('/index_02_03')
def index_02_03():
    return render_template('02_03.html', title='Grid')

@app.route('/index_02_04')
def index_02_04():
    return render_template('02_04.html', title='Grid')

@app.route('/index_02_05')
def index_02_05():
    return render_template('02_05.html', title='Grid')

@app.route('/index_02_06')
def index_02_06():
    return render_template('02_06.html', title='Grid')

@app.route('/index_02_07')
def index_02_07():
    return render_template('02_07.html', title='Grid')

@app.route('/index_03_01')
def index_03_01():
    return render_template('03_01.html', title='Grid')
