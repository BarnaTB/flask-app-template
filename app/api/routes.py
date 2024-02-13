from flask import Blueprint, jsonify, request
from sqlalchemy import and_, or_
from app import limiter
from app import database
from app.src.model import Recommender


route_blueprint = Blueprint("api", __name__)

@route_blueprint.route("/", methods=['GET'])
@limiter.limit("100/day;20/hour;5/minute")
def index():

    response_data = {
        "message": "Done did it!!!"
    }
    return jsonify(response=response_data), 200


@route_blueprint.app_errorhandler(404)
def not_found(e):
    return jsonify(error=404, text=str(e)), 404
