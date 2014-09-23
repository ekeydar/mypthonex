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

LOGGER = logging.getLogger("tornado.access")
logging.Formatter.converter = time.gmtime # force UTC in logger

define('debug', default=False, group='application', help="run in debug mode (with automatic reloading)")
define('port',default=9000,group='application')

class MyWebSocketHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True
    def open(self):
        print 'opened'
        self.write_message('welcome')
        
    def on_close(self):
        print 'closed'

    def on_message(self, message):
        print 'on_message message = %s' % (message)
        self.write_message(message[::-1])

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

