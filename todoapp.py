from flask import Flask, render_template, request, redirect, session
import re

app = Flask(__name__)

to_do_list = []

@app.route('/')
def to_do():
    try:
        error = session.get('error')
        return render_template('to_do_list.html', to_do_list = to_do_list, error = error)
    except:
        return render_template('to_do_list.html', to_do_list = to_do_list, error = '')

@app.route('/submit', methods = ['POST'])
def submit():
    session['error'] = ''

    task = request.form['task']
    email = request.form['email']
    priority = request.form['priority']
    
    valid_priority = ['Low','Medium','High']
    valid_email = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

    if priority in valid_priority and re.search(valid_email,email):
        to_do_list.append([task,email,priority])
        return redirect('/')
    else:
        session['error'] = 'You have either entered an invalid email address or priority for the task!'
        return redirect('/')

@app.route('/clear', methods = ['POST'])
def clear():
    to_do_list.clear()
    return redirect('/')

if __name__ == '__main__':
    app.secret_key = 'sekrit'
    app.run()