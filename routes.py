from flask import Flask, render_template, json, request,flash, redirect
import prog
from flask_wtf.csrf import CSRFProtect, CSRFError
from forms import LoginForm
from logform import LoginForm2
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


@app.route('/signup', methods=['GET', 'POST'])
def my_form_post():
    form = LoginForm2()
    if form.validate_on_submit():
        dh.newUser(form.data['email'],form.data['password'],form.data['phone'])
        return redirect('/')

    return render_template('signup.html', title='Sign In', form=form)



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

@app.route('/ml')
def showsumm():
    dh.bargraph()
    return render_template('show_summ.html')

if __name__ == "__main__":
    app.debug = True
    app.run(port=5002)

