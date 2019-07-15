from flask import request, jsonify, request, Response, abort, send_file
from app.controllers.Slack import Slack
from app.authenticator.auth import require_apikey

def slack_routes(app):
    
    #TODO: Figure out how to not create a new App each call
    @app.route("/api/slack", methods=['GET'])
    @require_apikey
    def slackCollection():
        resources = Slack().listResources()
        return jsonify(resources)

    #TODO: Figure out how to not create a new App each call
    @app.route("/api/slack/<resource>", methods=['GET'])
    @require_apikey
    def slackResource(resource):

        response = Slack().runResource(resource)
        if("content" in response and "type" in response):
            if(response.get("type") == "file"):
                return send_file(response.get("content"))
            elif(response.get("type") == "text"):
                return jsonify(response)
        else :
            return jsonify(response), 404