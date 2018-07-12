# _*_ coding: utf-8 _*_

from marshmallow import Schema, fields
from utility.mysqlHelper import db

class Cafe4(db.Model):
    __tablename__ = "cafe4"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category = db.Column(db.Enum("tea", "coffee", name="category_name"), nullable=False, default="coffee")
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Numeric(precision=5, scale=2), nullable=False)

    def __repr__(self):
        return "Cafe4(%d, %s, %s, %5.2f)" % (self.id, self.category, self.name, self.price)

class Cafe4Schema(Schema):
    class Meta:
        fields = ('id', 'category', 'name', 'price')

def load_db2(db):
    db.drop_all()
    db.create_all()

    db.session.add_all([
        Cafe4(name='aaa', price=3.99),
        Cafe4(name='bbb', price=4.98),
        Cafe4(name='ccc', price=5.98),
        Cafe4(name='ddd', price=6.98),
    ])
    db.session.commit()



def create_table(db):
    db.create_all()
    db.session.commit()
    pass

def add_one(db, **kwargs):
    db.session.add(Cafe4(**kwargs))
    db.session.commit()

def add_all(db, *args):
    pass
