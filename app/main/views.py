from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required
from . import main
from ..models import User

@main.route('/')
def landingpage():

    return render_template('landingpage.html')

@main.route('/timeline')
@login_required
def timeline():

    return render_template('timeline.html')

@main.route('/user/profile/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template('profile.html', user = user)
