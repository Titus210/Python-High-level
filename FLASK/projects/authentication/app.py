import bcrypt
from flask import Flask, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, InputRequired, ValidationError
from flask_wtf import FlaskForm


app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'mysecretkey'


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Username"})
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={
                        "placeholder": "Email"})
    password = PasswordField('Password', validators=[DataRequired(), Length(
        min=8)], render_kw={"placeholder": "Password"})
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(
    ), EqualTo('password')], render_kw={"placeholder": "Confirm Password"})
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        existing_username = User.query.filter_by(
            username=username.data).first()
        if existing_username:
            raise ValidationError(
                'That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                'That email is taken. Please choose a different one.')


class loginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={
                        "placeholder": "Email"})
    password = PasswordField('Password', validators=[DataRequired(), Length(
        min=8)], render_kw={"placeholder": "Password"})
    submit = SubmitField('Login')


# Application Routes
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login')
def login():
    return render_template('login.html', form=RegisterForm())


@app.route('/register')
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        new_user = User(username=form.username.data,
                        email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html', form=RegisterForm())


@app.route('/forgot-password')
def forgot_password():
    return render_template('forgot-password.html')


@app.route('/reset-password')
def reset_password():
    return render_template('reset-password.html')


if __name__ == '__main__':
    app.run(debug=True)
