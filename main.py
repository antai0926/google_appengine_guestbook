import webapp2

import guestbook_handler

app = webapp2.WSGIApplication([
    ('/', guestbook_handler.MainPage),
    ('/sign', guestbook_handler.Guestbook),
], debug=True)