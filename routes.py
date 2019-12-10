# -*- coding: utf-8 -*-
from urllib import request

from flask import Blueprint, jsonify

from models import Vacancy, db, Category, Status

api = Blueprint('api', __name__, url_prefix='/api')
index = Blueprint('index', __name__, url_prefix='/')


@api.route('/vacancy')
def get_vacancys():
    return jsonify([(lambda vacancy: vacancy.json())(vacancy) for vacancy in Vacancy.query.all()])

@api.route('/vacancy/id/<int:vac_id>')
def get_vacancy(vac_id):
    vac = Vacancy.query.get(vac_id)
    return vac.json() if vac else ''


@api.route('/vacancy/add')
def add_vacancy():
    name = request.args.get('name')
    position = request.args.get('position')
    category_id = request.args.get('category_id')
    status_id = request.args.get('status_id')
    addArgs = Vacancy(name=name, position=position, category_id = category_id, status_id = status_id)
    db.session.add(addArgs)
    db.session.commit()
    return jsonify(addArgs.json())

@api.route('/category/add')
def add_category():
    name = request.args.get('name')
    addArgs = Category(name=name)
    db.session.add(addArgs)
    db.session.commit()
    return jsonify(addArgs.json())

@api.route('/status/add')
def add_status():
    name = request.args.get('name')
    addArgs = Status(name=name)
    db.session.add(addArgs)
    db.session.commit()
    return jsonify(addArgs.json())


@index.route('/')
@index.route('/index')
def get_index():
    return '''
    <html>
        <head>
            <title>Gorshkov - app</title>
        </head>
        <body>
            <div style="text-align:center;">
                <h1 style="font-style:italic; color: red">Hello!</h1>
                <h3>API</h3>
                <a href="./api/vacancy">vacancy</a>
            </div>
        </body>
    </html>
           '''
