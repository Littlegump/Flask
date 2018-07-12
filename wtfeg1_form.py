# _*_ coding: utf-8 _*_

import os, binascii


from flask_wtf import FlaskForm
from wtforms import Form, StringField, PasswordField
from wtforms.validators import InputRequired, Length


class loginForm(FlaskForm):
    username = StringField("USERNAME:", validators=[InputRequired(), Length(min=4, max=6)])
    password = PasswordField("PASSWORD:", validators=[Length(min=4, max=6)])
