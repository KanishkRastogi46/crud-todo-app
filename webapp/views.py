from flask import Blueprint , render_template , request , flash , url_for , redirect , jsonify
from flask_login import login_required , current_user
from .models import Todo , User
from . import db
import json

views = Blueprint("view" , __name__)


# home route
@views.route("", methods=['GET','POST'])
@login_required
def home():
    if request.method=="POST":
        title = request.form.get('title')
        content = request.form.get('content')

        if len(content.strip())<1:
            flash("Don't leave the content area empty", category="error")
        else:
            # creating new todo
            new_todo = Todo(title=title, content=content, user_id=current_user.id)
            db.session.add(new_todo)
            db.session.commit() 

    return render_template("index.html", user=current_user), 200


@views.route('/create-todo')
@login_required
def create_todo():
    return render_template("create_note.html" , user=current_user)


@views.route('/update-todo/<int:id>', methods=['GET','POST'])
@login_required
def update_todo(id):
    todo = Todo.query.get(int(id))
    if request.method=="POST":
        todo.title = request.form.get("title")
        todo.content = request.form.get("content")
        db.session.commit()
    return render_template('update_note.html' , todo=todo , user=current_user)


# delete todo
@views.route("/delete-todo", methods=['POST'])
@login_required
def delete_todo():
    data = request.json
    todo = Todo.query.get(data['id'])
    if todo:
        if todo.user_id==current_user.id:
            db.session.delete(todo)
            db.session.commit()
    return jsonify({})