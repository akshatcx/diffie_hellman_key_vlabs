#Controller file including all the routes

from flask import Blueprint, render_template, request, jsonify
from .api import helper
from .models import Quiz
from .models import db

import json

main=Blueprint('main', __name__)

#Index Route
@main.route('/')
def index():
    return render_template("Introduction.html")

#Introduction route
@main.route('/introduction')
def introduction():
    return render_template("Introduction.html")

#Theory Route
@main.route('/theory')
def theory():
    return render_template("Theory.html")

#Objective Route
@main.route('/objective')
def objective():
    return render_template("Objective.html")

#Experiment Route
@main.route('/experiment')
def experiment():
    return render_template("Experiment.html")

#Manual Route
@main.route('/manual')
def manual():
    return render_template("Manual.html")

#Quiz Route
@main.route('/quizzes')
def quizzes():
    return render_template("Quizzes.html")

#Procedure Route
@main.route('/procedure')
def procedure():
    return render_template("Procedure.html")

#Further Reading Route
@main.route('/further_reading')
def further_reading():
    return render_template("Further Readings.html")

#Feedback Route
@main.route('/feedback', methods=['GET','POST'])
def feedback():
    return render_template("Feedback.html")
    pass

#API Routes for generating values for the experiment which return json objects

#GENP generates a prime number of l bits (taken as an url argument)
@main.route('/api/genp')
def genp():
    l=0
    l=int(str(request.args.get('bits')))

    #helper file contains the required function genp
    p = str(helper.genp(l))
    return json.dumps({'prime': p })

#GENG generates the generator of l-1 bits (taken as an url argument)
@main.route('/api/geng')
def geng():
    p=int(str(request.args.get('prime')))

    #helper file contains the required function geng
    g=str(helper.geng(p))
    return json.dumps({'generator': g })

#GENPK generates a private key by taking the prime number as an url argument
@main.route('/api/private_key')
def private_key():
    p=int(str(request.args.get('prime')))

    #helper file contains the required function genpk
    pk=str(helper.genpk(p))
    return json.dumps({'private_key' : pk })

#CALG(a,b,p) calculates (a^b)%p
@main.route('/api/calg')
def calg():

    p=int(str(request.args.get('p')))
    a=int(str(request.args.get('a')))
    b=int(str(request.args.get('b')))
    g=int(str(request.args.get('g')))

    #Values are generated using calg function from helper file
    Ga = str(helper.calg(g,a,p))
    Gb = str(helper.calg(g,b,p))
    Gab = str(helper.calg(Gb,a,p))
    Gba = str(helper.calg(Ga,b,p))

    ret = {
        'Ga' : Ga,
        'Gb' : Gb,
        'Gab' : Gab,
        'Gba' : Gba,
    }

    return json.dumps(ret)

#Route to add the quiz entries to the database
@main.route('/addanswers', methods = ['POST'])
def addAnswers():
    db.create_all()
    answer1 = request.form['q1']
    answer2 = request.form['q2']
    answer3 = request.form['q3']
    answer4 = request.form['q4']
    try:
        if( answer1 != "" and answer2!="" and answer3 != "" and answer4 != ""):
            Answer = Quiz(answer1, answer2, answer3, answer4)
            db.session.add(Answer)
            db.session.commit()
    except:
        flash('Please fill in all the answers',"error")
    return json.dumps(True)

@main.route('/answers', methods = ['GET'])
def getall():
    new = Quiz.query.all()
    return jsonify(sentence=[curr.id for curr in new], q1=[curr.ans_q1 for curr in new], q2=[curr.ans_q2 for curr in new], q3=[curr.ans_q3 for curr in new], q4=[curr.ans_q4 for curr in new], date=[curr.date_time for curr in new])
