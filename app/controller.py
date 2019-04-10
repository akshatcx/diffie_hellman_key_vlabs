from flask import Blueprint, render_template, request
#from .models import db

import json

main=Blueprint('main', __name__)

@main.route('/introduction')
def introduction():
    return "hi"

@main.route('/theory')
def theory():
    pass

@main.route('/objective')
def objective():
    pass

@main.route('/experiment')
def experiment():
    pass

@main.route('/manual')
def manual():
    pass

@main.route('/quizzes')
def quizzes():
    pass

@main.route('/procedure')
def procedure():
    pass

@main.route('/further_readings')
def further_reading():
    pass

@main.route('/feedback', methods=['GET','POST'])
def feedback():
    pass

@main.route('/api')
def api():
    pass




