from flask import Blueprint , request , render_template , redirect , url_for , flash
from .models import User
from . import db
from werkzeug.security import generate_password_hash , check_password_hash
from flask_login import login_user , logout_user , login_required , current_user


auth = Blueprint("auth" , __name__)


# signup route
@auth.route('/register', methods=['GET','POST'])
def register():
    if request.method=="POST":
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm-password')

        existing_user = User.query.filter_by(username=username, email=email).first()

        if username.strip()=="" or email.strip()=="" or password.strip()=="" or confirm_password.strip()=="":
            flash("Please fill the form correctly", category="error")
        elif password!=confirm_password:
            flash("Password doesn't matches with confirm password", category="error")
        elif len(password)<6:
            flash("Password should be greater or eqauls to 6 characters", category="error")
        elif email.strip()=="" or email.index("@")==-1:
            flash("Invalid email", category="error")
        elif len(username)<3:
            flash("Username should be greater or eqauls to 3 characters", category="error")
        elif existing_user:
            flash("User already exists", category="error")
        else:
            new_user = User(email= email , username = username,  password = generate_password_hash(password , method='pbkdf2' , salt_length=16))
            db.session.add(new_user)
            db.session.commit()
            login_user(user=new_user, remember=True)
            flash("User registered successfully", category="success")
            return redirect(url_for("view.home"))

    return render_template("register.html")


# login route
@auth.route('/login' , methods=['GET','POST'])
def login():
    if request.method=="POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username.strip()=="" or password.strip()=="":
            flash("Please fill the form correctly", category="error")
        else:
            user_exists = User.query.filter_by(username=username).first()
            if user_exists:
                if check_password_hash(user_exists.password, password):
                    flash("User logged in successfully", category="success")
                    login_user(user=user_exists, remember=True)
                    return redirect(url_for("view.home"))
            else:
                flash("Username doesn't exists or incorrect user", category="error")
    return render_template("login.html")


# logout route
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))