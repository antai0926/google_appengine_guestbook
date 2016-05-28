from google.appengine.ext import ndb

from models import Author_modle


class Greeting(ndb.Model):
    """A main model for representing an individual Guestbook entry."""
    author = ndb.StructuredProperty(Author_modle.Author)
    content = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)


def save_greeting(parent, author, content):
    greeting = Greeting(parent=parent, author=author, content=content)
    greeting.put()
