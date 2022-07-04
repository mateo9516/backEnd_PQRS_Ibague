from distutils.debug import DEBUG
from distutils.log import debug
from flask import Flask, jsonify, render_template, request, session, url_for
from werkzeug.utils import redirect
from werkzeug.exceptions import abort


## Rutas / modulos del app
from routes import radicaciones

#######################

app = Flask(__name__)

def page_not_found(error):
    return "<h1>Not found page</h1>", 404

if __name__ == '__main__':
       
    app.register_blueprint(radicaciones.main, url_prefix='/api/obtenerDf')

    app.register_error_handler(404, page_not_found)

    app.run()