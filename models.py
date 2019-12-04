from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Men(db.Model):
    __tablename__ = 'mens'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    job = db.Column(db.String(120))

    def json(self):
        return {"id": self.id, "name": self.name, "job": self.job, }
