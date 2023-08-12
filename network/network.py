from flask.views import MethodView
from flask_smorest import abort, Blueprint
from flask import render_template, request, url_for
# from schemas import CloudSchema
# from models import CloudModel
# from sqlalchemy.exc import SQLAlchemyError
# from db import db

blp = Blueprint("Network", __name__, template_folder='templates' )

@blp.route('/network_form')
def get():
    return render_template("network/network_view.html")