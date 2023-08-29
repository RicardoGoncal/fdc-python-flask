from flask_smorest import abort, Blueprint
from flask import render_template, request, redirect
from models import CloudModel, RequestModel
from sqlalchemy.exc import SQLAlchemyError
from db import db
from time import sleep

blp = Blueprint("Cloud", __name__, template_folder='templates' )

@blp.route('/cloud_form', methods=['GET','POST'])
def cloud_view():
    return render_template("cloud/cloud_view.html")


@blp.route('/nova_demanda_cloud', methods=['GET','POST'])
def nova_demanda():
    if request.method == 'POST':
        global dados_nova_demanda # Variavel global pra uso
        dados_nova_demanda = request.form # Coleta os dados do Formulario da parte de nova demanda(infos comuns)
        return redirect('cloud_form') # leva para a parte dois do formulario

    demand_type = 'nova_demanda_cloud' # passa essa informacao no html de nova demanda para referenciar essa rota de cloud quando for acionada
    return render_template("general/novaDemanda.html", data=demand_type)


@blp.route('/processar_form_cloud', methods=['GET','POST'])
def processar_form():
    
    if request.method == 'POST':

        dados_demanda_cloud = request.form # Coleta os dados do Formulario da parte de cloud
        demand_type = "cloud" # Tipo de demanda
        
        try:

            # Gravar dados da request
            nova_demanda = RequestModel(**dict(dados_nova_demanda))
            nova_demanda.demandType = demand_type # Atribui o tipo de demanda que esta sendo aberta
            db.session.add(nova_demanda)
            db.session.commit() # grava primeiro as informações comuns do pedido para poder associar o ID com a tabela de cloud depois
            sleep(5)
            
            # Gravar dados de cloud
            cloud_form = CloudModel(**dict(dados_demanda_cloud))
            cloud_form.requestIdFk = nova_demanda.requestId # Adiciona o valor do ID da request para a chave estrangeira na tabela de cloud
            db.session.add(cloud_form)

            db.session.commit() # Finaliza com a gravação das informações de cloud
        except Exception as e:
            db.session.rollback()
            print(e)

        # form = CloudModel(**form)

        # print(form.inputPPM)
        # print(form.inputTypeCust)
        # print(form.inputProjectDemandName)
        # print(form.inputDemandPEPCC)
        # print(form.inputManager)
        # print(form.inputArchitect)
        # print(form.inputEntityResposible)
        # print(form.inputItOt)
        # print(form.inputSpecialReq)
        # print(form.inputHelpText)
        # print(form.radioRg)

        # print(form.inputResourceGroup )
        # print(form.inputNeedUsersAccess )
        # print(form.inputProjectName )
        # print(form.inputResponsible )
        # print(form.inputWorkType )
        # print(form.inputRegion )
        # print(form.radioTransition )
        # print(form.inputDate )

        # print(form.radioSp)
        # print(form.inputHLD)
        # print(form.inputFunctionArea)
        # print(form.inputAzureResources)
        # print(form.radioNet)
        # print(form.inputDescribeConfig)

        # try:
        #     db.session.add(form)
        #     db.session.commit()
        # except Exception as e:
        #     db.session.rollback()
        #     print(e)

    return "retornar a pagina do formulario ou a inicial"


# @blp.route('/ver_bd')
# class VerBd(MethodView):
#     @blp.response(200, CloudSchema(many=True)) # Decorator
#     def get(self):
#         return CloudModel.query.all()
