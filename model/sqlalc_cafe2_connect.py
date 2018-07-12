#!/usr/bin/env python
# _*_ coding: utf-8  _*_

from sqlalchemy import create_engine
#from ..config.config import conn_mysql_dict



conn_mysql_dict = dict(
    host='localhost',
    port=3306,
    user='testuser',
    password='testpwd',
    db='testdb'
)

url = 'mysql://{user}:{password}@{host}:{port}/{db}'
#print url.format(**conn_mysql_dict)
engine = create_engine(url.format(**conn_mysql_dict))

engine.echo = True

conn = engine.connect()
conn.execute('DROP TABLE IF EXISTS cafe2')
conn.execute('''CREATE TABLE IF NOT EXISTS cafe2 (
                    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
                    category ENUM('tea', 'coffee') NOT NULL,
                    name VARCHAR(20) NOT NULL,
                    price DECIMAL(5,2) NOT NULL,
                    PRIMARY KEY(id)
                )''')


# Insert one record
conn.execute('''INSERT INTO cafe2 (category, name, price) VALUES
                  ('coffee', 'Espresso', 3.19)''')

# Insert multiple records
conn.execute('''INSERT INTO cafe2 (category, name, price) VALUES
                  ('coffee', 'Cappuccino', 3.29),
                  ('coffee', 'Caffe Latte', 3.39),
                  ('tea', 'Green Tea', 2.99),
                  ('tea', 'Wulong Tea', 2.89)''')

for row in conn.execute('SELECT * FROM cafe2'):
    print(row)

conn.close()


#if __name__ == "__main__":
    #main()

#class sqlHelper(object):
