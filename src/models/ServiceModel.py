from marshmallow import fields, Schema
from . import db
class ServiceModel(db.Model):
    # Service Model
    # table name
    __tablename__ = "services"
    srv_id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    srv_name = db.Column(db.String(80), nullable=False)
    srv_description = db.Column(db.Text, nullable=False)
    srv_category = db.Column(db.String(80), nullable=False)
    srv_unit = db.Column(db.String(30), nullable=False)
    srv_price = db.Column(db.Float, nullable=False)
    # class constructor
    def __init__(self, data):
        # Class constructor
        self.srv_name = data.get("srv_name")
        self.srv_description = data.get("srv_description")
        self.srv_category = data.get("srv_category")
        self.srv_unit = data.get("srv_unit")
        self.srv_price = data.get("srv_price")
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
class ServiceSchema(Schema):
    # Service Schema
    srv_id = fields.Int(required=True, dump_only=True)
    srv_name = fields.Str(required=True, dump_only=True)
    srv_description = fields.Str(required=True, dump_only=True)
    srv_category = fields.Str(required=True, dump_only=True)
    srv_unit = fields.Str(required=True, dump_only=True)
    srv_price = fields.Int(required=True, dump_only=True)