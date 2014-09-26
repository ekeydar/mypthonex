import datetime
import json

import tornado.web
import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.options
import tornado.httpclient
from tornado.options import options,define
import logging
import time

LOGGER = logging.getLogger("tornado.access")
logging.Formatter.converter = time.gmtime # force UTC in logger

define('debug', default=True, group='application', help="run in debug mode (with automatic reloading)")
define('port',default=9000,group='application')

class MyWebSocketHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        try:
            self.uid = int(self.get_argument('uid'))
        except Exception,e:
            self.write_error(400,'integer uid is mandatory')
        if self.uid > 10:
            LOGGER.info('uid = %d - closing' % self.uid)
            self.close(code=400)
        LOGGER.info('uid = %s: opened successfully',self.uid)
        self.write_message('welcome %s' % self.uid)


        
    def on_close(self):
        self.info('uid = %s: closed',self.uid)

    def on_message(self, message):
        LOGGER.info('uid = %s: on_message message = %s', self.uid, message)
        self.write_message('%s said: %s' % (self.uid,message))

class MyApplication(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/open/',MyWebSocketHandler)
        ]
        
        tornado.web.Application.__init__(self, handlers, **options.group_dict('application'))
            
def main():
    tornado.options.parse_command_line()
    app = MyApplication()
    server = tornado.httpserver.HTTPServer(app)
    server.listen(options.port)
    LOGGER.info('options.port = %s' % options.port)
    tornado.ioloop.IOLoop.instance().start()
 
    
if __name__ == '__main__':
    main()

