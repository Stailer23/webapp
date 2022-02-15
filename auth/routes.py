from flask import Blueprint, render_template, url_for, flash
from auth.forms import LoginForm, RegistaryForm

auth = Blueprint('auth', __name__, template_folder='templates', static_folder='static')

menu = [{'name': 'Главная', 'url': 'index'},
        {'name': 'Написать пост', 'url': 'index'},
        {'name': 'О проекте', 'url': 'index'},
        {'name': 'Авторизация', 'url': '.login'}]

@auth.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    return render_template('/auth/login.html', title='Авторизация', menu=menu, form=form)

@auth.route('/registary', methods=['POST', 'GET'])
def registary():
    form = RegistaryForm()
    return render_template('/auth/registary.html', title='Регистрация', menu=menu, form=form)