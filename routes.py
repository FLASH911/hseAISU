from flask import Blueprint, jsonify

from models import Employee, db

api = Blueprint('api', __name__, url_prefix='/api')
index = Blueprint('index', __name__, url_prefix='/')

@api.route('/employee')
def get_employee():
    return jsonify([(lambda employee: employee.json()) (employee) for employee in Employee.query.all()])

#@api.route('/position')
#def get_position():
   # return jsonify([(lambda men: men.json()) (men) for men in position.query.all()])

@api.route('/men/id/<int:men_id>')
def get_men (men_id):
    men = Employee.query.get(men_id)
    return men.json() if men else ''

@api.route('/men/name/<string:men_name>;<string:men_job>')
def put_men (men_name, men_job):
    addVars = Employee(name=men_name, job=men_job)
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
                <a href="./api/employee">Employee</a>
            </div>
        </body>
    </html>
           '''