from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Email, DataRequired, Length, EqualTo

class LoginForm(FlaskForm):
    email = StringField('Email: ', validators=[Email("Некорректный email")])
    psw = PasswordField('Пароль: ', validators=[DataRequired(), Length(min=4, max=100, message='Пароль должен быть от 4 до 100 символов')])
    remember = BooleanField('Запомнить меня', default=False)
    submit = SubmitField('Войти')

class RegistaryForm(FlaskForm):
    user = StringField('Login: ', validators=[Length(min=4, max=20, message='Логин должен быть от 4 до 20 символов')])
    email = StringField('Email: ', validators=[Email('Неккоректный email')])
    psw = PasswordField('Пароль: ', validators=[DataRequired(), Length(min=4, max=100, message='Пароль должен быть от 4 до 100 символов')])
    rep_psw = PasswordField('Повторите пароль: ', validators=[DataRequired(), EqualTo('psw', message='Пароли не совпадают')])
    submit = SubmitField('Зарегестрироваться')
