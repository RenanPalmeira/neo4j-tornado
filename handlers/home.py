import tornado.web
from pyneo4j import GraphDatabase, Node

graph = GraphDatabase(user='neo4j', password='python') 

class HomeHandler(tornado.web.RequestHandler):
	def get(self, *args, **kwargs):

		humans = Node('Human').all()
		self.render('index.html', humans=humans)

class NodeHandler(tornado.web.RequestHandler):
	def get(self, *args, **kwargs):
		_id = args[0]
		human = Node('Human').get(id=_id)
		self.render('node.html', human=human)