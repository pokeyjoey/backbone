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

@app.route('/index_03_02')
def index_03_02():
    return render_template('03_02.html', title='Grid')

@app.route('/index_03_03')
def index_03_03():
    return render_template('03_03.html', title='Grid')

@app.route('/index_03_04')
def index_03_04():
    return render_template('03_04.html', title='Grid')

@app.route('/index_03_05')
def index_03_05():
    return render_template('03_05.html', title='Grid')

@app.route('/index_03_06')
def index_03_06():
    return render_template('03_06.html', title='Grid')

@app.route('/index_03_07')
def index_03_07():
    return render_template('03_07.html', title='Grid')

@app.route('/index_03_09')
def index_03_09():
    return render_template('03_09.html', title='Grid')

@app.route('/index_03_08')
def index_03_08():
    return render_template('03_08.html', title='Grid')

@app.route('/index_04_01')
def index_04_01():
    return render_template('04_01.html', title='Grid')

@app.route('/index_04_02')
def index_04_02():
    return render_template('04_02.html', title='Grid')

@app.route('/index_04_03')
def index_04_03():
    return render_template('04_03.html', title='Grid')

@app.route('/index_04_04')
def index_04_04():
    return render_template('04_04.html', title='Grid')

@app.route('/index_05_01')
def index_05_01():
    return render_template('05_01.html', title='Grid')

@app.route('/index_05_02')
def index_05_02():
    return render_template('05_02.html', title='Grid')

@app.route('/index_05_03')
def index_05_03():
    return render_template('05_03.html', title='Grid')

@app.route('/index_05_04')
def index_05_04():
    return render_template('05_04.html', title='Grid')

