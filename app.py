from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/scene1', methods=('GET', 'POST'))
def scene1():
    if request.method == 'POST':
        return redirect('scene2')
    return render_template('scene1.html')


@app.route('/scene2')
def scene2():
    return render_template('scene2.html')
