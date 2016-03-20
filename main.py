import webapp2
import guestbook

app = webapp2.WSGIApplication([
    ('/', guestbook.MainPage),
    ('/sign', guestbook.Guestbook),
], debug=True)