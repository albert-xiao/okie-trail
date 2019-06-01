from typing import List

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

names: List[str] = []


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/scene1', methods=('GET', 'POST'))
def scene1():
    if request.method == 'POST':
        nms = request.form.getlist('name')
        if len(nms) == 5:
            global names
            names = nms
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



if __name__ == '__main__':
    app.run()
