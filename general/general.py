from flask.views import MethodView
from flask import  Blueprint, render_template, url_for
from sqlalchemy.exc import SQLAlchemyError
from db import db
from models import CloudModel, NetworkModel, RequestModel


blp = Blueprint("General", __name__,template_folder='templates' )


@blp.route('/')
def homepage():
    # return "Teste do mal do mal"
    return render_template("general/homepage.html")


@blp.route('/todos_pedidos')
def pedidos():

    # Faz uma query em todos os pedidos do BD
    items = RequestModel.query.all()

    return render_template("general/todos_pedidos.html", items=items)


@blp.route('/pedidos_cloud')
def pedidos_cloud():

    # Faz uma query em todos os pedidos do BD
    items = CloudModel.query.all()

    return render_template("general/pedidos_cloud.html", items=items)


@blp.route('/pedidos_network')
def pedidos_network():

    # Faz uma query em todos os pedidos do BD
    items = NetworkModel.query.all()

    return render_template("general/pedidos_network.html", items=items)