from typing import List

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

state = {'names': [], 'money': 0}


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/scene1', methods=('GET', 'POST'))
def scene1():
    if request.method == 'POST':
        names = request.form.getlist('name')
        if len(names) == 5:
            state['names'] = names
            return redirect('scene2')
    return render_template('scene1.html')


@app.route('/scene2')
def scene2():
    return render_template('scene2.html')


@app.route('/scene3')
def scene3():
    return render_template('scene3.html')


@app.route('/scene4')
def scene4():
    return render_template('scene4.html')


@app.route('/scene5', methods=('GET', 'POST'))
def scene5():
    if request.method == 'POST':
        print(request.form['decision'])
        return redirect('scene6')
    return render_template('scene5.html')


@app.route('/scene6')
def scene6():
    return render_template('scene6.html', state=state)


@app.route('/scene7')
def scene7():
    return render_template('scene7.html')


if __name__ == '__main__':
    app.run()
