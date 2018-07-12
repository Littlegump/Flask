# _*_ coding: utf-8 _*_

from sqlalchemy import create_engine, Column, Integer, String, Enum, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

Base = declarative_base()

class Cafe2(Base):
    __tablename__ = "cafe2"
    id = Column(Integer, primary_key=True, autoincrement=True)
    category = Column(Enum('tea', 'coffee', name='cat_enum'))
    name = Column(String(50))
    price = Column(Numeric(precision=5, scale=2))

    def __init__(self, category, name, price, id=None):
        if id:
            self.id = id
        self.category = category
        self.name = name
        self.price = price

    def __repr__(self):
        return "Cafe2(%d, %s, %s, %5.2f)" % (
            self.id, self.category, self.name, self.price)


conn_mysql_dict = dict(
    host='localhost',
    port=3306,
    user='testuser',
    password='testpwd',
    db='testdb'
)

engine = create_engine("mysql://{user}:{password}@{host}:{port}/{db}".format(**conn_mysql_dict))
engine.echo = True
engine.echo = False

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

session = scoped_session(sessionmaker(bind=engine))

dbsession = session()

print "allOne"
print ""
dbsession.add(Cafe2("coffee", "Cappuccino", 3.29))
dbsession.commit()

print "allall"
print ""
dbsession.add_all([Cafe2("tea", "black_tea", 3.23),Cafe2("tea", "india_tea", 9.24)])
dbsession.commit()


print "queryall"
for instance in dbsession.query(Cafe2).all():
    print instance.category, instance.name, instance.price


print "query_order"
instance = dbsession.query(Cafe2).order_by(Cafe2.name).first()
print instance

print "query_definitily"
for instance in dbsession.query(Cafe2).filter_by(category='coffee').all():
    print instance
    print instance.__dict__

print "query greater"
for instance in dbsession.query(Cafe2).filter(Cafe2.price > 3.00).all():
    print instance

instance_to_delete = dbsession.query(Cafe2).filter_by(name="Cappuccino").all()
for ins in instance_to_delete:
    dbsession.delete(ins)
dbsession.commit()
