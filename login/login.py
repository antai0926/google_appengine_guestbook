
from google.appengine.api import users


def is_can_see():
    if users.get_current_user():
        email = users.get_current_user().email()
        if email == 'sky25apple1129@gmail.com' or email == 'antai0926@gmail.com':
            return True
    return False
