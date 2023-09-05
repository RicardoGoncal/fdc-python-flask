from flask.views import MethodView
from flask import  Blueprint, render_template, url_for, redirect, request
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql import text
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


@blp.route('/todos_pedidos/busca_por_nome', methods=['GET','POST'])
def busca_por_nome():

    if request.method == 'POST':
        pesquisa_nome = request.form['pesquisar']
        query = f"requests.[inputManager] = '{pesquisa_nome}'"

        items = RequestModel.query.filter(text(query)).all()

        return render_template("general/todos_pedidos.html", items=items)



# @blp.route('/todos_pedidos/busca_por_id')
# def busca_por_id():
#     pass


# @blp.route('/pedidos_cloud/busca_por_id')
# def busca_id_cloud():
#     pass


# @blp.route('/pedidos_network/busca_por_id')
# def busca_id_net():
#     pass