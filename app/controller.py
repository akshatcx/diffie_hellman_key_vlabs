from flask import Blueprint, render_template, request
#from .models import db

import json

main=Blueprint('main', __name__)

@main.route('/introduction')
def introduction():
    return render_template("Introduction.html")
@main.route('/theory')
def theory():
    return render_template("Theory.html")

@main.route('/objective')
def objective():
    return render_template("Objective.html")

@main.route('/experiment')
def experiment():
    return render_template("Experiment.html")

@main.route('/manual')
def manual():
    return render_template("Manual.html")

@main.route('/quizzes')
def quizzes():
    return render_template("Quizzes.html")

@main.route('/procedure')
def procedure():
    return render_template("Procedure.html")

@main.route('/further_reading')
def further_reading():
    return render_template("Further Readings.html")

@main.route('/feedback', methods=['GET','POST'])
def feedback():
    return render_template("Feedback.html")
    pass

@main.route('/api')
def api():
    pass
