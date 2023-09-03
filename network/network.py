from flask_smorest import abort, Blueprint
from flask import render_template, request, redirect
from models import NetworkModel, RequestModel
from sqlalchemy.exc import SQLAlchemyError
from db import db
from time import sleep
import random

blp = Blueprint("Network", __name__, template_folder='templates' )

@blp.route('/network_form', methods=['GET','POST'])
def network_view():
    return render_template("network/network_view.html")


@blp.route('/nova_demanda_network', methods=['GET','POST'])
def nova_demanda():
    if request.method == 'POST':
        global dados_nova_demanda # Variavel global pra uso
        dados_nova_demanda = request.form # Coleta os dados do Formulario da parte de nova demanda(infos comuns)
        return redirect('network_form') # leva para a parte dois do formulario

    demand_type = 'nova_demanda_network' # passa essa informacao no html de nova demanda para referenciar essa rota de netwoprk quando for acionada
    return render_template("general/novaDemanda.html", data=demand_type)


@blp.route('/processar_form_network', methods=['POST'])
def processar_form():
    random.seed()

    if request.method == 'POST':
        dados_demanda_net = request.form # Coleta os dados do Formulario da parte de network
        demand_type = "network" # Tipo de demanda

        # Gerar um numero para o chamado
        numero_demanda = random.randint(1,1000)
        
        try:
            # Gravar dados da request
            nova_demanda = RequestModel(**dict(dados_nova_demanda))
            nova_demanda.requestId = numero_demanda
            nova_demanda.demandType = demand_type # Atribui o tipo de demanda que esta sendo aberta
            nova_demanda.requestIdFkNetwork = numero_demanda
            db.session.add(nova_demanda)
            # db.session.commit() # grava primeiro as informações comuns do pedido para poder associar o ID com a tabela de network depois
            sleep(5)
            
            # Gravar dados de cloud
            net_form = NetworkModel(**dict(dados_demanda_net))
            net_form.requestIdNetwork = numero_demanda
            # net_form.requestIdFk = nova_demanda.requestId # Adiciona o valor do ID da request para a chave estrangeira na tabela de network
            db.session.add(net_form)

            db.session.commit() # Finaliza com a gravação das informações de network
        except Exception as e:
            db.session.rollback()
            print(e)

    # return "retornar a pagina do formulario ou a inicial"
    return redirect('/')