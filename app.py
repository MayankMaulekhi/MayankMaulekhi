
from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'secret123'

cust_dict = {123: ["mayank", "123", "5412"]}
login_dict = {'jk': '12'}

def random_id():
    while True:
        rand = random.randint(10000, 99999)
        if rand not in cust_dict:
            return rand

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        uname = request.form['username']
        pwd = request.form['password']
        if uname in login_dict and login_dict[uname] == pwd:
            session['username'] = uname
            return redirect(url_for('dashboard'))
        else:
            return render_template("login.html", msg="Invalid login")
    return render_template("login.html")

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))

    message = ""
    if request.method == 'POST':
        action = request.form['action']

        if action == 'Add':
            name = request.form['name']
            age = request.form['age']
            phone = request.form['phone']
            if age.isdigit() and 10 < int(age) < 125 and phone.isdigit():
                cid = random_id()
                cust_dict[cid] = [name, age, phone]
                message = "Customer added!"
            else:
                message = "Invalid age or phone."

        elif action == 'Delete':
            cid = int(request.form['cust_id'])
            if cid in cust_dict:
                del cust_dict[cid]
                message = "Customer deleted"
            else:
                message = "Customer not found"

        elif action == 'Update':
            cid = int(request.form['cust_id'])
            name = request.form['name']
            age = request.form['age']
            phone = request.form['phone']
            if cid in cust_dict:
                cust_dict[cid] = [name, age, phone]
                message = "Customer updated"
            else:
                message = "Customer not found"

    return render_template("dashboard.html", customers=cust_dict, msg=message)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
