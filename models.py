import datetime

from flask import Markup
from markdown import markdown
from micawber import parse_html
from peewee import *

from app import db, oembed


class Note(Model):
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)
    archived = BooleanField(default=False)

    class Meta:
        database = db

    def html(self):
        html = markdown(self.content)
        return Markup(html)

    @classmethod
    def public(cls):
        return (Note
                .select()
                .where(Note.archived == False)
                .order_by(Note.timestamp.desc()))
