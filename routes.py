from flask import Flask, render_template, json, request,flash, redirect
import prog
from flask_wtf.csrf import CSRFProtect, CSRFError
from forms import LoginForm
import os
import random

dh = prog.Dhobi()
dh.distance()

csrf = CSRFProtect()

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

# csrf = CSRFProtect(app)
# app.config.from_object('config.settings')

csrf.init_app(app)

@app.route('/')
def main():

    return render_template('main_index.html')

@app.route('/signup')
def sign():
    return render_template('index.html')

@app.route('/signup', methods=['POST'])
def my_form_post():
    print('form: '+request.form)
    text = [request.form['text'],request.form['password'],request.form['submit']]
    print(text)
    return text
    # return render_template('index.html')
    # return redirect('/')

# @app.route('/table')
# def showTable():
#     form = LoginForm()
#     return render_template('form.html', title='Details', form=form)

@app.route('/table', methods=['GET', 'POST'])
def dispTable():
    form = LoginForm()
    if form.validate_on_submit():
        l = []
        for a in form.data:
            if a not in ['csrf_token','submit']:
                l.append(form.data[a])

        # print(l)


        with open('Table.csv','a+') as f:
            f.write('\n'+','+str(random.randint(111,999))+','+','.join(l)+'\n')
        dh.distance()

        # flash('Login requested for user {}, remember_me={}'.format(
            # form.username.data, form.remember_me.data))


        return redirect('/')

    return render_template('form.html', title='Details', form=form)

@app.route('/graph')
def showGraph():
    return render_template('path.html')

@app.route('/path')
def showPath():
    return render_template('show_path.html')


if __name__ == "__main__":
    app.debug = True
    app.run(port=5002)

