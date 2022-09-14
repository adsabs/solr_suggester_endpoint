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
    def query_solr_suggester(params):
       current_app.logger.info("Querying autocomplete with the following parameters: {}".format(params))
       return requests.get(url=current_app.config.get("SOLR_SUGGEST_URL"), params = params)
    
    @staticmethod
    def restructure_solr_response(solr_response):
        return solr_response
    
    @staticmethod
    def get_GET_params(request, types={}):
        """
        Attempt to coerce GET params data into json from request, falling
        back to the raw data if json could not be coerced.
        :param request: flask.request
        :param types: types that the incoming request object must cohere to
        """
        try:
            get_params = request.args.to_dict()
        except ValueError:
            msg = "Failed to parse input parameters: {}. Please confirm request is properly formatted.".format(request)
            raise ValueError(msg)
        if "q" in get_params.keys():
            query = get_params.pop("q")
            current_app.logger.info("Query is {}".format(query))
            get_params["suggest.q"] = str(query).strip()

            return get_params
        else:
            msg = "Query: {} is missing parameter 'q'. Please confirm request conforms to ADS /search syntax.".format(get_params)
            raise ValueError(msg)

class AuthorSuggesterView(SuggesterView):
    @classmethod
    def query_author_suggester(query, **kwargs):
        return requests.get()

    def get():
        return 0

class AuthorNormSuggesterView(SuggesterView):
    suggester = 'normsuggester'
    params = {'suggest': 'true', 'suggest.build': 'true', 'suggest.dictionary': suggester, 'suggest.count': '20', 'wt': 'json'}

    @classmethod
    def query_author_norm_suggester(self, request):
        user_params = self.get_GET_params(request)
        for key in user_params.keys():
            self.params[key] = user_params[key]
        solr_response = self.query_solr_suggester(params=self.params)
        
        if solr_response.status_code == 200:
            current_app.logger.info("Response is {}".format(solr_response.json()))
            terms = solr_response.json()['suggest'][self.params['suggest.dictionary']][self.params['suggest.q']]['suggestions']
            current_app.logger.info("Received suggestions: {}".format(terms))
            suggestions ={"suggestions": []}
            for i in terms:
                suggestions['suggestions'].append(i["term"])
            current_app.logger.info("Suggestions are : {}".format(suggestions['suggestions']))
            
        else:
            current_app.logger.error("Failed to retrieve suggestions with error: {}".format(solr_response.status_code))
            suggestions = {"suggestions": []}

        return suggestions

    def get(self):
        response = self.query_author_norm_suggester(request)
        return response, 200


class UATSuggesterView(SuggesterView):
    def get(self):
        current_app.logger.info("Test endpoint reached")
        return {"response": "Hit endpoint"}, 200