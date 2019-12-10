from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

db = SQLAlchemy()


class Vacancy(db.Model):
    __tablename__ = 'Vacancy'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    position = db.Column(db.String(120))
    category_id = db.Column(db.Integer, ForeignKey('Category.id'))
    category = relationship('Category')
    status_id = db.Column(db.Integer, ForeignKey('Status.id'))
    status = relationship('Status')

    def json(self):
        return {"id": self.id, "position": self.position, "category": self.category.json(), "status": self.status.json()}

class Category(db.Model):
    __tablename__ = 'Category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    #job = db.Column(db.String(120))

    def json(self):
        return {"id": self.id, "name": self.name}

class Status(db.Model):
    __tablename__ = 'Status'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    #job = db.Column(db.String(120))

    def json(self):
        return {"id": self.id, "name": self.name}

