from flask.views import MethodView
from flask import  Blueprint, render_template, url_for
from sqlalchemy.exc import SQLAlchemyError
from db import db
from models import CloudModel


blp = Blueprint("Home", __name__,template_folder='templates' )


@blp.route('/')
def homepage():
    # return "Teste do mal do mal"
    return render_template("general/homepage.html")


@blp.route('/pedidos')
def pedidos():

    # Faz uma query em todos os pedidos do BD
    items = CloudModel.query.all()

    return render_template("general/pedidos.html", items=items)