from flask import Flask

appvar = Flask(__name__)
#appvar.config.from_object(Config)

from . import routes
