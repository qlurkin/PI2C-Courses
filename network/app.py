import cherrypy

class Web:
	@cherrypy.expose
	def index(self, name="World"):
		with open('test.html') as file:
			content = file.read()
		return content.format(name)

	@cherrypy.expose
	def login(self, user, pswd):
		return f"hello {user}, your password is {pswd}"

cherrypy.quickstart(Web(), '', 'server.conf')