
import web
from web.app import create_app
from web import settings
from werkzeug import DebuggedApplication

flask_app = create_app(settings)

if flask_app.config['DEBUG']:
    flask_app.debug = True
    flask_app = DebuggedApplication(flask_app, evalex=True)

app = flask_app
