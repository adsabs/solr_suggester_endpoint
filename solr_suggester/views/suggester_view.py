"""
Base view
"""
from unittest.mock import NonCallableMagicMock
import uuid
import base64

from ..views import DEFAULT_LIBRARY_NAME_PREFIX, DEFAULT_LIBRARY_DESCRIPTION, \
    USER_ID_KEYWORD
from flask import request, current_app, make_response, jsonify
from flask_restful import Resource
import requests

class SuggesterView(Resource):
    @staticmethod
    def query_solr_suggester(query, suggester, **kwargs):
        requests.get(url=current_app.config.get("SOLR_URL"))
