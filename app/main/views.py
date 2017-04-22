from flask import render_template, session, redirect, url_for, current_app

from .. import db

from ..models import User
from . import main
from .forms import NameFrom

@main.route('/',methods=['GET','POST'])
def index():
    form = NameFrom()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username = form.name.data)
            db.session.add(user)
            session['known'] = False

        else:
            session['known'] = True
        session['name'] = form.name.data
    return  render_template('index.html',form=form,name = session.get('name'),
                            known=session.get('known',False))