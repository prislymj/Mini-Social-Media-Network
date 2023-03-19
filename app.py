from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_wtf import csrf, FlaskForm
from flask_sqlalchemy import SQLAlchemy
from form import EditProfileForm
from functools import wraps

#app = Flask(__name__)
app = Flask(__name__, static_folder='static', static_url_path='/static')
app.secret_key = 'testkey'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:prisly2001@localhost/newapp1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:prisly2001@localhost:3306/newapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)

class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    dob = db.Column(db.Date, nullable=True)
    phone_number = db.Column(db.String(20), nullable=True)
    bio = db.Column(db.String(200), nullable=True)
    image_url = db.Column(db.String(200), nullable=True)


@app.before_first_request
def create_tables():
    db.create_all()
    
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        user = User(name=name, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        flash('User added to database', 'success')
        return redirect(url_for('profile'))
    else:
        return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email, password=password).first()
        if user:
            session['user_id'] = user.id
            return 'Logged in successfully!'
        else:
            return 'Invalid email or password.'
    else:
        return render_template('login.html')
    
def login_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return func(*args, **kwargs)
    return decorated_function

@app.route('/profile')
@login_required
def profile():
    user_id = session['user_id']
    user = User.query.get(user_id)
    return f'Welcome {user.name}!'

@app.route('/create_profile', methods=['GET', 'POST'])
def create_profile():
    if request.method == 'GET':
        return render_template('create_profile.html')
    elif request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        dob = request.form['dob']
        phone_number = request.form['phone_number']
        bio = request.form['bio']
        image_url = request.form['image_url']
        profile = UserProfile(name=name, email=email, dob=dob, phone_number=phone_number, bio=bio, image_url=image_url)
        db.session.add(profile)
        db.session.commit()
        return redirect(url_for('profile', profile_id=profile.id))

@app.route('/profile/edit', methods=['GET', 'POST'])
@login_required
def edit_profile():
    user_id = session['user_id']
    user = User.query.get(user_id)
    form = EditProfileForm(obj=user)

    if form.validate_on_submit():
        form.populate_obj(user)
        db.session.commit()
        flash('Profile updated successfully.')
        return redirect(url_for('profile'))

    csrf_token = csrf.generate_csrf()
    return render_template('edit_profile.html', user=user, form=form, csrf_token=csrf_token)

@app.route('/search')
def search():
    query = request.args.get('query')
    if query:
        # Search for users based on the query
        users = User.query.filter(User.name.ilike(f'%{query}%')).all()
    else:
        # If no query is provided, return all users
        users = User.query.all()
    return render_template('search.html', query=query, users=users)
if __name__ == '__main__':
    app.run(debug=True)
