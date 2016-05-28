
from google.appengine.ext import ndb


class Author(ndb.Model):
    """Sub model for representing an author."""
    identity = ndb.StringProperty(indexed=False)
    email = ndb.StringProperty(indexed=False)


def save_author(identity, email):
    author = Author(identity=identity, email=email)
    author_key = author.put()
    # return key if another kind's property need to save this
    return author_key




