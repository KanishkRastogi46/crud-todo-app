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


# delete todo
@views.route("/delete-todo", methods=['POST'])
@login_required
def delete_todo(todo_id):
    data = json.loads(request.data)
    todo = Todo.query.get(data.todo_id)
    if todo:
        if todo.user_id==current_user.id:
            db.session.delete(todo)
            db.session.commit()
    return jsonify({})