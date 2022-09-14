"""
Base view
"""
from unittest.mock import NonCallableMagicMock
import uuid
import base64

from flask import request, current_app, make_response, jsonify
from flask_restful import Resource
import requests

class SuggesterView(Resource):
    @staticmethod
    def query_solr_suggester(query, suggester, **kwargs):
       return requests.get(url=current_app.config.get("SOLR_URL"))
    
    @staticmethod
    def restructure_solr_response(solr_response):
        return solr_response

class AuthorSuggesterView(SuggesterView):
    @classmethod
    def query_author_suggester(query, **kwargs):
        return requests.get()

    def get():
        return 0

class AuthorNormSuggesterView(SuggesterView):
    @classmethod
    def query_author_norm_suggester(query, **kwargs):
        return requests.get()

    def get():
        return 0

class UATSuggesterView(SuggesterView):
    @classmethod
    def query_uat_suggester(query, **kwargs):
        return requests.get()

    def get():
        return 0