"""
Application
"""

import logging.config

from werkzeug.serving import run_simple
from .views import AuthorSuggesterView, UATSuggesterView, AuthorNormSuggesterView
from flask_restful import Api
from flask_discoverer import Discoverer
from adsmutils import ADSFlask

def create_app(**config):
    """
    Create the application and return it to the user
    :return: application
    """

    app = ADSFlask(__name__, static_folder=None, local_config=config or {})
    app.url_map.strict_slashes = False

    # Register extensions
    api = Api(app)
    Discoverer(app)
    
    # Add the end resource end points
    api.add_resource(AuthorSuggesterView,
                     '/autocomplete/author',
                     methods=['GET'])

    api.add_resource(AuthorNormSuggesterView,
                     '/autocomplete/author_norm',
                     methods=['GET'])

    api.add_resource(UATSuggesterView,
                     '/autocomplete/uat',
                     methods=['GET'])
                
    return app


if __name__ == '__main__':
    run_simple('0.0.0.0', 5000, create_app(), use_reloader=False, use_debugger=False)