from flask import Flask , render_template , url_for , flash , redirect
from forms import registrationForm , LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'u0A$7r@Y%gqP1!kXz#N5dF&Lc*Bt9eWj'

posts = [
    {
        'author':'mayank gfd ',
        'title': 'blog post 1',
        'content' : 'first content',
        'dateposted':'march 30 2190'
    },
    {
        'author':'rahhul gfd ',
        'title': 'blog post 2',
        'content' : 'first content',
        'dateposted':'march 3 2190'
    }
]

@app.route("/")
def hello():
    return render_template("home.html",posts= posts)

@app.route("/about")
def about():
    return render_template("about.html", title= 'about')

@app.route("/register", methods =["GET","POST"])
def register():
    form = registrationForm()
    if form.validate_on_submit():
        flash(f'account created for {form.username.data}!' , 'success')
        return redirect(url_for('hello'))
    return render_template('register.html', title = register , form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title = 'login' , form=form)

if __name__ == "__main__":
    app.run(debug=True)
