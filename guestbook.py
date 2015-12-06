#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.appengine.api import users
from google.appengine.ext.webapp import template

import cgi
import webapp2
import logging

MAIN_PAGE_HTML = """\
<html>
  <title>Guestbook</title>
  <meta name="robots" content="noindex,nofollow">
  <link type="text/css" rel="stylesheet" href="/stylesheets/main.css" />
  <body>
    <form action="/sign" method="post">
      <div><textarea name="content" rows="30" cols="100"></textarea></div>
      <div><input type="submit" value="Sign Guestbook"></div>
    </form>
  </body>
</html>
"""

SIGN_PAGE_HTML = """\
<html>
  <title>Guestbook</title>
  <link type="text/css" rel="stylesheet" href="/stylesheets/main.css" />
</html>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        logging.info("See the logging!")

        # Checks for active Google account session
        user = users.get_current_user()

        if user:
            self.response.headers['Content-Type'] = 'text/html; charset=utf-8'
            self.response.write('Hello, ' + user.nickname())
        else:
            self.redirect(users.create_login_url(self.request.uri))

        self.response.write(MAIN_PAGE_HTML)

class Guestbook(webapp2.RequestHandler):
    def post(self):
        self.response.write(SIGN_PAGE_HTML)
        self.response.write('<html><body>You wrote:<pre>')
        self.response.write(cgi.escape(self.request.get('content')))
        self.response.write('</pre></body></html>')

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/sign', Guestbook),
 ], debug=True)
