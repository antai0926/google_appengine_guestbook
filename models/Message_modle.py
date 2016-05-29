from google.appengine.ext import ndb

from models import Author_modle


class Message(ndb.Model):
    """A main model for representing an individual Guestbook entry."""
    author = ndb.StructuredProperty(Author_modle.Author)
    content = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)


def save_message(parent, author, content):
    greeting = Message(parent=parent, author=author, content=content)
    greeting.put()
