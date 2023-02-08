from starlette.applications import Starlette
from starlette.middleware.wsgi import WSGIMiddleware

from . import api, web

app = Starlette()

app.mount("/api", api.app)
app.mount("/", WSGIMiddleware(web.app))
