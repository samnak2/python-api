from marshmallow import fields, Schema
from . import db
class ServiceModel(db.Model):
    # Service Model
    # table name
    __tablename__ = "services"
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(80), nullable=False)
    unit = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Float, nullable=False)
    # class constructor
    def __init__(self, data):
        # Class constructor
        self.name = data.get("name")
        self.description = data.get("description")
        self.category = data.get("category")
        self.unit = data.get("unit")
        self.price = data.get("price")
    def save(self):
        db.session.add(self)
        db.session.commit()
    def update(self, data):
        for key, item in data.items():
            setattr(data, key, item)
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    @staticmethod
    def get_all_services():
        return ServiceModel.query.all()
    @staticmethod
    def get_one_service():
        print("get one service")
        return ServiceModel.query.get(1)
    def __repr__(self):
        return "<id {}>".format(self.id)