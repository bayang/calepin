import datetime

from flask import Markup
from markdown import markdown
from peewee import *
from pyembed.markdown import PyEmbedMarkdown
from pyembed.core.consumer import PyEmbedConsumerError

from app import db


class Note(Model):
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)
    archived = BooleanField(default=False)

    class Meta:
        database = db

    def html(self):
        try:
            html = markdown(self.content, extensions=[PyEmbedMarkdown()])
            return Markup(html)
        except PyEmbedConsumerError as e:
            modif_note = self.content.replace(self.content[0:23], "<")
            modif_note = modif_note.replace(self.content[-1], ">")
            html = markdown(modif_note)
            return Markup(html)

    @classmethod
    def public(cls):
        return (Note
                .select()
                .where(Note.archived == False)
                .order_by(Note.timestamp.desc()))
