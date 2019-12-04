from flask import Blueprint, jsonify

from models import Men, db

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/mens')
def get_mens():
    return jsonify([(lambda men: men.json()) (men) for men in Men.query.all()])

@api.route('/men/id/<int:men_id>')
def get_men (men_id):
    men = Men.query.get(men_id)
    return men.json() if men else ''

@api.route('/men/name/<string:men_name>;<string:men_job>')
def put_men (men_name, men_job):
    addVars = Men(name=men_name, job=men_job)
    db.session.add(addVars)
    db.session.commit()
    return jsonify(addVars.json())
