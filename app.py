# -*- coding: utf-8 -*-
from flask import Flask

from models import db, Vacancy, Category, Status
from routes import api, index

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.register_blueprint(api)
app.register_blueprint(index)
db.init_app(app)
with app.app_context():
    db.create_all()
    locksmith = Category(name='Слесарь')
    engineer = Category(name='Engineer')
    manager = Category(name='ИТР')
    director = Category(name='Director')
    laborer = Category(name='Laborer')
    db.session.add(manager)
    db.session.add(locksmith)
    db.session.add(engineer)
    db.session.add(director)
    db.session.add(laborer)
    db.session.commit()
    now = Status(name='Active')
    archive = Status(name='Archive')
    db.session.add(now)
    db.session.add(archive)
    db.session.commit()
    db.session.add(Vacancy(position='Директор', category_id = director.id, status_id = now.id))
    db.session.add(Vacancy(position='Оператор котельной на завод', category_id = laborer.id, status_id = now.id))
    db.session.add(Vacancy(position='Java программист (Middle)', category_id = engineer.id, status_id = archive.id))
    db.session.commit()

if __name__ == '__main__':
    app.run()