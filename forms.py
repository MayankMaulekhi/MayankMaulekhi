from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField , SubmitField , BooleanField
from wtforms.validators import data_required,  Length, Email , EqualTo


class registrationForm(FlaskForm):
    username = StringField('username',
                           validators = [data_required(),Length(min=2 ,max=20)])
    email = StringField('email',
                           validators=[data_required(), Email()])
    password = PasswordField('password',
                             validators=[data_required()])
    confirmpassword = PasswordField('confirmpassword',
                                    validators=[data_required() , EqualTo('password')])
    submit= SubmitField('sign up')

class LoginForm(FlaskForm):
    email = StringField('email',
                           validators=[data_required(), Email()])
    password = PasswordField('password',
                             validators=[data_required()])
    remember = BooleanField('remember me')
    Submit= SubmitField('sign up')