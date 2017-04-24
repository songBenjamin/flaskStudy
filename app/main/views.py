from flask import render_template, session, redirect, url_for, current_app, flash
from flask_login import login_required, current_user
from .. import db

from ..models import User
from . import main
from .forms import NameFrom, EditProfileFrom

@main.route('/',methods=['GET','POST'])
def index():
    return  render_template('index.html')

@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html',user=user)

@main.route('/edit-profile',methods=['GET','POST'])
@login_required
def edit_profile():
    form = EditProfileFrom()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.location = form.location.data
        current_user.about_me = form.about_me.data
        db.session.add(current_user)
        flash('Your profile has been updated.')
        return redirect(url_for('.user',username=current_user.username))
    form.name.data = current_user.name
    form.location.data = current_user.location
    form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', form=form)