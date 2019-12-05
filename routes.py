from flask import Blueprint, jsonify

from models import Men, db

api = Blueprint('api', __name__, url_prefix='/api')
index = Blueprint('index', __name__, url_prefix='/')

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

@index.route('/')
@index.route('/index')
def get_index():
    return '''
    <html>
        <head>
            <title>Gorshkov - app</title>
        </head>
        <body>
            <div style="background: green; text-align:center;">
                <h1 style="font-style:italic; color: red">Hello!</h1>
                <h3>API</h3>
                <a href="./api/mens">Mens</a>
            </div>
        </body>
    </html>
           '''