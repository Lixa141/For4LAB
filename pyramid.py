from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from jinja2 import Environment, FileSystemLoader,Template

env = Environment(loader=FileSystemLoader('.'))

def index(request):
     template = env.get_template('index.html').render(link="""<a href="http://localhost:8000/about/aboutme.html">Index </a>""")
return Response(template)

def about(request):
    template = env.get_template('about/aboutme.html').render(link="""<a href="http://localhost:8000/index.html"> About me </a>""")    
return Response(template)

if __name__ == '__main__':
    config = Configurator()
    configurator.add_route("aboutme",'/about/aboutme.html')
    configurator.add_view(AboutMe,route_name='aboutme')
    configurator.add_route('index', '/index.html')
    configurator.add_view(Index, route_name='index')
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8000, app)
    server.serve_forever()
    
