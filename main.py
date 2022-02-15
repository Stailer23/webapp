from flask import Flask, render_template, url_for
import os
from flask_login import LoginManager
from auth.routes import auth
from werkzeug.security import generate_password_hash, check_password_hash

# configure
DEGUG = True
SECRET_KEY = 'FSFREGDFGDSsdfdfsdfggrreg432rasd3232EF4gfdgfg54232432f'

app = Flask(__name__)
app.config.from_object(__name__)
# app.config.update(dict(DATABASE=os.path.join(app.root_path, 'mydb.db')))
# login_manager = LoginManager(app)

app.register_blueprint(auth, url_prefix='/auth')

menu = [{'name': 'Главная', 'url': 'index'},
        {'name': 'Написать пост', 'url': 'index'},
        {'name': 'О проекте', 'url': 'index'},
        {'name': 'Авторизация', 'url': 'auth.login'}]

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="1231", menu=menu)






if __name__ == '__main__':
    app.run(debug=DEGUG)
