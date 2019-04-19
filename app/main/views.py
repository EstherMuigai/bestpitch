from flask import render_template,request,redirect,url_for
from . import main

@main.route('/')
def landingpage():

    return render_template('landingpage.html')

@main.route('/timeline')
def timeline():

    return render_template('timeline.html')