from datetime import datetime
from flask import Flask, jsonify, request

app = Flask(__name__)
config = app.config.from_envvar('APP_SETTINGS')

from application.models import db, Task

with app.app_context():
    db.init_app(app)
    db.create_all()

def get_task(task_id):
    return db.session.query(Task).filter_by(id=task_id).first_or_404()


@app.route("/tasks")
def tasks_list():
    tasks = db.session.query(Task).all()
    return jsonify(tasks=[i.serialize for i in tasks])

@app.route("/tasks/<int:task_id>")
def task_by_id(task_id):
    task = get_task(task_id)
    return jsonify(task=task.serialize)

@app.route("/tasks/post", methods=['POST'])
def task_post():
    text = request.form.get('text')
    date = request.form.get('date')
    date_format = datetime.strptime(date, '%Y-%m-%d %H:%M')

    db.session.add(Task(text=text, date=date_format))
    db.session.commit()
    return jsonify()


if __name__ == '__main__':


    app.run()
