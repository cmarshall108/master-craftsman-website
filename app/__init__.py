from flask import Flask

app = Flask(__name__)
#appvar.config.from_object(Config)

from . import routes
