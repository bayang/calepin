#!/usr/bin/python3.4
# -*- coding:utf-8 -*-

import os

from flask import Flask
from peewee import SqliteDatabase

APP_ROOT = os.path.dirname(os.path.realpath(__file__))
DATABASE = os.path.join(APP_ROOT, 'notes.db')
DEBUG = False
SECRET_KEY = '4F\x1e\xf4\x18R5\xbeZ\x8c\x02\xe7]\x8fW\x06\x1d\xea\xee\xc6\xe9\x98\x8e'
MYLOGIN = os.environ.get('CALEPIN_LOGIN')
MYPASS = os.environ.get('CALEPIN_PASS')

app = Flask(__name__)
app.config.from_object(__name__)
db = SqliteDatabase(app.config['DATABASE'], threadlocals=True)
