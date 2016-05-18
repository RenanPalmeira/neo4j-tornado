import os
import hashlib
import tornado.web

from handlers.home import HomeHandler, NodeHandler

class Application(tornado.web.Application):
	def __init__(self):
		urls = [
			(r'/', HomeHandler),
			(r'/(\d+)', NodeHandler),
		]

		settings = dict(
			cookie_secret = hashlib.md5('python-love-neo4j').hexdigest(),
			template_path = os.path.join(os.path.dirname(__file__), 'templates'),
			static_path = os.path.join(os.path.dirname(__file__), 'static'),
			xsrf_cookies = True,
			debug = True,
		)
		tornado.web.Application.__init__(self, urls, **settings)

if __name__ == '__main__':
	application = Application()
	application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()