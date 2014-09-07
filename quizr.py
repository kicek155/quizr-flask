# -*- coding: utf-8 -*-
"""
Quizr - a quiz application created with Flask.
"""

import os
import io
import random
import pdb
from flask import Flask, session, request, render_template, redirect, url_for
from time import time
from distribution_example.csv_loader import get_question
# from distribution_example.csv_loader import get_question


# create app and initialize config
app = Flask(__name__)

app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='development key',
))
app.config.from_envvar('QUIZR_SETTINGS', silent=True)

@app.route('/', methods=['GET', 'POST'])
def welcome_page():
    """
    Welcome page - quiz info and username form.
    """
    
    username = session.get('username')
    reset()
    if request.method == 'POST':
        if not username:
            session['username'] = request.form['username']
        if username:
            return redirect(url_for('question_page'))
    return render_template('welcome.html', username=username)


@app.route('/pytanie', methods=['GET', 'POST'])
def question_page():
    """
    Quiz question page - show question, handle answer.
    """
    question_start_time = session.get('start_time')
    question_last_answer = session.get('last_answer')
    counter = session.get('counter')
    if not counter:
        session['counter'] = 0
    if session['counter'] < 5:
        if session['counter'] > 0:
            check_answer(question_start_time, question_last_answer, counter)
        session['counter'] += 1
        question = _get_question()
        session['start_time'] = time()
        session['last_answer'] = question.pop()
        answers = {}
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        for k, a in enumerate(question):
            if k > 0:
                answers[letters[k-1]] = a
        # answers = zip(letters, question[1:-1]
        return render_template('question.html', question=question[0], answers=answers, counter=session['counter']),
    else:
        check_answer(question_start_time, question_last_answer, counter)
        return redirect(url_for('result_page'))


@app.route('/wynik')
def result_page():
    """
    Last page - show results.
    """
    results = session.get('results')
    points = 0
    if results:
        for k,p in results.items():
            points += p['points']
    return render_template('results.html', results=results, points=points),

def _get_question():
    # if username:
    doned = session.get('doned')
    # with io.open('data/quiz.csv', mode='r', encoding='utf8') as f:
    #     questions = f.read()
    #     questions = questions.split('\n')
    questions = get_question('data/quiz.csv')
    if not doned:
        session['doned'] = []
    random.seed(random.random())
    number = random.randrange(0, len(questions)-1)
    while number in session['doned']:
        number = random.randrange(0, len(questions)-1)
    session['doned'].append(number)
    return questions[number].split(';')
     
def reset():
    doned = session.get('doned')
    counter = session.get('counter')
    results = session.get('results')
    if doned:
        del(session['doned'])
    if counter:
        del(session['counter'])
    if results:
        del(session['results'])
        
def check_answer(question_start_time, question_last_answer, counter):
    stop_time = time()
    _time = int(stop_time-question_start_time)
    results = session.get('results')
    if not results:
        session['results'] = {}
    
    '''
     3 punkty za poprawną odpowiedź w czasie krótszym niż 10 sekund od wyświetlenia pytania
     * 2 punkty za poprawną odpowiedź w pomiędzy 10 a 30 sekundą od wyświetlenia pytania
     * 1 punkt za poprawną odpowiedź w czasie powyżej 30 sekund
    '''
    points = 0
    if question_last_answer == request.form['answer']:
        if _time < 10:
            points = 3
        elif _time >10 and _time < 30:
            points = 2
        else:
             points = 1
    session['results'][counter] = {
            'correct': question_last_answer,
            'your': request.form['answer'],
            'time': _time,
            'points': points
        }
    
    
if __name__ == '__main__':
    app.run(host=os.environ['IP'], port=int(os.environ['PORT']))
