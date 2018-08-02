#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import os, binascii
import simplejson as json
import time
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, escape, jsonify
from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, validators, DateTimeField, TextAreaField, IntegerField
from wtforms.validators import DataRequired
from wtfeg1_form import loginForm
from model.sqlself import sqlSelf
from model.admin import Admin
from config.config import run_flask_dict
from model.flask_sqlalchemy_cafe3 import load_db, Cafe3, Cafe3Schema, db2_cafe3
from utility.mysqlHelper import db
from model.sqlalchemy_cafe4_ajaxjson import load_db2, Cafe4, Cafe4Schema



app = Flask(__name__)

# 下面将如何设置app.config
# 1. app.config["SECRET_KEY"] =  binascii.hexlify(os.urandom(24))
# 2. app.config.from_object("config.config")
# 3. 如下
#app.config.from_object("config.config.ConfigDevelopment")
app.config.from_object("config.config.ConfigProduction")
db.init_app(app) # bind sqlalchemy to this flask app

# create the db tables and records inside a temporary test context
# this test_request_context() tell falsk to behaves as if it is handling a request
# with app.test_request_context():
#     load_db(db)

with app.test_request_context():
    load_db2(db)

class myForm(FlaskForm):
    #"""docstring for myForm."""
    name =  StringField('name', validators=[DataRequired()])
    #def __init__(self, arg):
        #super(myForm, self).__init__()

#class MyForm(FlaskForm):
    #name = StringField('name', validators=[DataRequired()])
#

def show_the_login_form():
    pass

def do_the_login():
    pass

def log_the_user_in(user):
    session['username'] = user
    return True

def verify_login(user, pwd):
    return ((user == "gzyinkaixuan") and (pwd == "redhat"))

@app.route('/mysql/<name>')
def mysql(name):
    if name == "version":
        sql = sqlSelf()
        sql_version = sql.get_db_version()
        return "SQL version is : %s" % dict(sql_version)['VERSION()']
    elif name == "insert":
        sql = sqlSelf()
        #params = ("coffee", "Espresso", 3.12)
        data = [('coffee', 'Cappuccino', 0.29),
                ('coffee', 'Caffe Latte', 11.39),
                ('tea', 'Green Tea', 0.99),
                ('tea', 'Wulong Tea', 0.89)]
        a = sql.insertIterm(data)
        return "rslt is %s " % a
    elif name == "getOne":
        sql = sqlSelf()
        params = (str(3.12))
        a = sql.getOne(params)
        return "rslt is %s " % a
    else:
        return "nothing"

@app.route('/post/<int:post_id>')
def post(post_id):
    return 'Post %d\n method is %s' % (post_id, str(request.method))

@app.route('/serverinfo')
def serverinfo():
    return render_template('serverinfo.html')

#@app.route('/login', methods=['GET', 'POST'])
#def login():
    #if request.method == 'POST':
        #do_the_login()
    #else:
        #show_the_login_form()

# 学习使用session
#
#
@app.route('/')
def index():
    if 'username' in session:
        #return "Login as %s" % escape(session['username'])
        return render_template("response.html", name=escape(session['username']))
    return redirect(url_for('login'))

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    #searchword = request.args.get('key', '')
    # 获取url中的key参数
    if request.method == 'POST':
        if verify_login(request.form['user'],
                        request.form['pwd']):
            log_the_user_in(request.form['user'])
            return redirect(url_for('index'))
        else:
            return "Invalid user/pwd."
    #return render_template('login.html', error=error)
    return render_template('form_example.html', error=error)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route('/submit', methods=["POST", "GET", "PUT"])
def submit():
    form = myForm()
    if form.validate_on_submit():
        print "haha"
        return redirect('/success')
    print "goto submit"
    return render_template('submit.html', form=form)

@app.route('/success', methods=["POST", "GET"])
def success():
    return "haha"


# 正式学习使用wtforms
@app.route('/wtfeg1')
def wtfeg1():
    _form = loginForm()
    return render_template("wtfeg1_form.html", form=_form)


@app.route('/login2', methods=['POST', 'GET'])
def login2():
    error = None
    #searchword = request.args.get('key', '')
    # 获取url中的key参数
    if request.method == 'POST':
        if verify_login(request.form['username'],
                        request.form['password']):
            log_the_user_in(request.form['username'])
            return redirect(url_for('index'))
        else:
            return "Invalid user/pwd."
    #return render_template('login.html', error=error)
    return render_template('form_example.html', error=error)

@app.route('/login3', methods=['GET', 'POST'])
def login3():
    form3 = loginForm()
    error = None
    if form3.validate_on_submit(): # POST request with valid input?
        if (form3.username.data == "peter" and form3.password.data == "peter"):
            log_the_user_in(form3.username.data)
            return redirect(url_for('index'))
        else:
            flash('Wrong user && pwd')
    return render_template("wtfeg3_form.html", form=form3)

@app.route('/b')
def b():
    return jsonify(key="value", key2="value2"), 200

@app.errorhandler(404)
def page_not_found(err):
    return render_template("404.html"), 404

@app.errorhandler(500)
def internal_server_error(err):
    return render_template("500.html"), 500

@app.before_request
def before_request():
    g.start_time = time.time()  # Store in g, applicable for this request and this user only

@app.teardown_request
def teardown_request(exception=None):
    time_taken = time.time() - g.start_time   # Retrieve from g
    print(time_taken)


@app.route('/context_processor', methods=["GET"])
def context_processor():
    return render_template('context_processor.html')

@app.context_processor
def template_context():
    '''Return a dictionary of key-value pairs,
       which will be available to all views in the context'''
    if 'username' in session:
        username = session['username']
    else:
        username = 'xxxxxxx'

    return {'version':88, 'username':username}

#@app.route('/submit', methods=('GET', 'POST'))
#def submit():
    #form = MyForm()
    #if form.validate_on_submit():
        #return redirect('/success')
    #return render_template('submit.html', form=form)

@app.route('/cafe3')
@app.route('/cafe3/<id>')
def cafe3(id=None):
    if id:
        _item_list = Cafe3.query.filter_by(id=id).all()
    else:
        _item_list = Cafe3.query.all()
        print _item_list
    return render_template("flask_sqlalchemy_cafe3.html", itemlist=_item_list)


# 使用marshmallow来get前端数据
item_schema = Cafe3Schema()
items_schema = Cafe3Schema(many=True)
@app.route('/api/iterm/', methods=["GET"])
@app.route('/api/iterm/<int:id>',methods=['GET'])
def query(id=None):
    if id:
        item = Cafe3.query.get(id)

        if item is None:
            return jsonify({"err_msg": ["We couldn't find iterm' '{}'".format(id)]}), 404
        else:
            rslt = item_schema.dump(item)
            print rslt
            return jsonify(rslt.data)
    else:
        items = Cafe3.query.limit(3)
        rslt = items_schema.dump(items)
        print rslt
        return jsonify(rslt.data)

# 使用ajax/json
cafe4_schema = Cafe4Schema()
cafe4_schemas = Cafe4Schema(many=True)
@app.route('/api/ajax/', methods=["GET"])
@app.route('/api/ajax/<int:id>', methods=["GET"])
def ajax(id=None):
    if id:
        item = Cafe4.query.get(id)
        if request.is_xhr:
            if item is None:
                return jsonify({"err_msg": ["We could not find item '{}'".format(id)]}), 404
            else:
                rslt = cafe4_schema.dump(item)
                return jsonify(rslt.data)
        else:
            # return web page
            if item is None:
                abort(404)
            else:
                return render_template('rest_ajax_cafe4.html')
    else:
        items = Cafe4.query.limit(3)
        if request.is_xhr:
            # return json
            rslt = cafe4_schemas.dump(items)
            return jsonify(rslt.data)
        else:
            # return webpage
            return render_template('rest_ajax_cafe4.html')

@app.route('/api/js/<int:id>', methods=['POST', 'GET'])
def js(id=1):
    if id == 1:
        return render_template("JSExAlertWrite.html"), 200
    elif id == 2:
        return render_template("JSExMoreEvents.html"), 200
    elif id == 3:
        # seperate html, css, JavaScript
        return render_template("JSExFiles.html"),200
    elif id == 4:
        return render_template("JQExEffect.html"), 200
    elif id == 5:
        return render_template("JQExAJAX.html"), 200
    elif id == 6:
        return render_template("JQExSelector.html"), 200
    elif id == 7:
        return render_template("JSExBasic.html"), 200
    elif id == 8:
        return render_template("JSExInnerHtml.html"), 200
    elif id == 9:
        return render_template("JSExLink.html"), 200

@app.route('/api/jq/<int:id>')
def jquery(id=1):
    if id == 1:
        return render_template("JQBasic.html"),200


@app.route('/apis', methods=['get'])
def nothing():
    return render_template("my_study.html"),200

@app.route('/api/bootstrap/<string:part>')
def bootstrap(part="base_css"):
    return render_template("bootstrap_%s.html" % part),200

@app.route('/api/html')
def html():
    return render_template('htmlbasic.html'), 200

if __name__ == "__main__":
    print app.url_map
    print app.config
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.run(**run_flask_dict)
    data = [('coffee', 'Cappuccino', 3.29),
            ('coffee', 'Caffe Latte', 3.39),
            ('tea', 'Green Tea', 2.99),
            ('tea', 'Wulong Tea', 2.89)]
