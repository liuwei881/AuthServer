# -*- coding: utf-8 -*-

import tornado
import json
from Route import db_session

class BaseHandler(tornado.web.RequestHandler):
    def __init__(self, *argc, **argkw):
        super(BaseHandler, self).__init__(*argc, **argkw)

    @property
    def db(self):
        return db_session

    def on_finish(self):
        self.db.close_all()
