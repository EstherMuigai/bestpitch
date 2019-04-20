from flask import render_template,request,redirect,url_for
from flask_login import login_required
from . import main

@main.route('/')
def landingpage():

    return render_template('landingpage.html')

@main.route('/timeline')
@login_required
def timeline():

    return render_template('timeline.html')