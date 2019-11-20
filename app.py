import random

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

state = {'names': ['A', 'B', 'C', 'D', 'E'],
         'money': 0,
         'food': 0,
         'day': 0,
         'eventno': 0,
         'took': False}

events = [0, 0, 1, 1, 'scene5', 0,
          1, 1, 1, 0, 'scene6',
          0, 1, 'scene7', 1, 'scene8']  # index starts at 1

scenario_weights = [
    20, 5, 20, 20, 20, 20
]


def state_change(resource, d):
    def f():
        state[resource] += d

    return f


scenarios = [
    lambda: None,
    state_change('money', -2.5),
    lambda: None,
    state_change('money', +.25),
    state_change('money', -2),
    state_change('food', -12),
    state_change('money', -.5)
]


def weighted_choice(choices):
    total = sum(choices)
    r = random.uniform(0, total)
    upto = 0
    for i, w in enumerate(choices):
        if upto + w >= r:
            return i
        upto += w


def init_events():
    for i, v in enumerate(events):
        if type(v) is not str and v == 1:
            events[i] = weighted_choice(scenario_weights) + 1


init_events()


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


@app.route('/scene4', methods=('GET', 'POST'))
def scene4():
    if request.method == 'POST':
        scenarios[events[state['eventno']]]()
        return redirect('trail', code=307)
    return render_template('scene4.html', state=state, scenario=events[state['eventno']])


@app.route('/scene5', methods=('GET', 'POST'))
def scene5():
    if request.method == 'POST':
        decision = request.form['decision']
        if decision == '0':
            state['names'].extend(('Mr. Ritchkey', 'Mrs. Ritchkey'))
            state['money'] += 23.20
            state['took'] = True
            state['food'] += 42
        elif decision == '1':
            state['money'] -= 5
        return redirect('trail', code=307)
    return render_template('scene5.html')


@app.route('/scene6', methods=('GET', 'POST'))
def scene6():
    if request.method == 'POST':
        del state['names'][2]
        return redirect('trail', code=307)
    return render_template('scene6.html', state=state)


@app.route('/scene7', methods=('GET', 'POST'))
def scene7():
    if not state['took']:
        return redirect('scene4')
    if request.method == 'POST':
        state['names'].pop(-1)
        state['names'].pop(-1)
        return redirect('trail', code=307)
    return render_template('scene7.html')


@app.route('/scene8')
def scene8():
    return render_template('scene8.html')


@app.route('/scene10')
def scene10():
    return render_template('scene10.html')


@app.route('/scene11')
def scene11():
    return render_template('scene11.html', state=state)


@app.route('/scene12')
def scene12():
    return render_template('scene12.html')


@app.route('/scene13')
def scene13():
    return render_template('scene13.html')


@app.route('/scene14')
def scene14():
    return render_template('scene14.html')


@app.route('/trail', methods=('POST',))
def trail():
    state['eventno'] += 1
    if type(events[state['eventno']]) is str:
        return redirect(events[state['eventno']])
    else:
        return redirect('scene4')


@app.route('/end')
def end():
    return render_template('end.html')


if __name__ == '__main__':
    app.run()
