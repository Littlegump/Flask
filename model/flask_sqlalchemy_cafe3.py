# _*_ coding: utf-8 _*_

from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema

db = SQLAlchemy()

class Cafe3Schema(Schema):
    class Meta:
        fields = ("id", "category", "name", "price")

class Cafe3(db.Model):
    __tablename__ = "cafe3"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category = db.Column(db.Enum("tea", "coffee", name="cat_enum"), nullable=False, default="coffee")
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Numeric(precision=5, scale=2, asdecimal=False), nullable=False, default=999.99)

    def __repr__(self):
        """describe itself"""
        return "Cafe3(%d, %s, %s, %5.2f)" % (self.id, self.category, self.name, self.price)

class db2_cafe3(db.Model):
    __bind_key__ = 'db2'
    __tablename__ = "db2_cafe3"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category = db.Column(db.Enum("tea", "coffee", name="cat_enum"), nullable=False, default="coffee")
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Numeric(precision=5, scale=2, asdecimal=False), nullable=False, default=999.99)

    def __repr__(self):
        """describe itself"""
        return "db2_(%d, %s, %s, %5.2f)" % (self.id, self.category, self.name, self.price)

def load_db(db):
    """Create database tables and insert records"""
    # Drop and re-create all the tables.
    db.drop_all()
    db.drop_all(bind=['db2'])
    db.drop_all(bind='db3')
    db.create_all()
    db.create_all(bind=['db2'])
    db.create_all(bind='db3')

    db.session.add_all([
        Cafe3(name='aaa', price=3.99),
        Cafe3(name='bbb', price=4.98),
        Cafe3(name='ccc', price=5.98),
        Cafe3(name='ddd', price=6.98),
    ], info={'bind_key': 'db2'})

    db.session.commit(bind='db2')

def insert_all():
    pass
