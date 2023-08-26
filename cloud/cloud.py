from flask_smorest import abort, Blueprint
from flask import render_template, request, redirect
from models import CloudModel, RequestModel
from sqlalchemy.exc import SQLAlchemyError
from db import db

blp = Blueprint("Cloud", __name__, template_folder='templates' )

@blp.route('/cloud_form', methods=['GET','POST'])
def cloud_view():
    return render_template("cloud/cloud_view.html")


@blp.route('/nova_demanda_cloud', methods=['GET','POST'])
def nova_demanda():
    if request.method == 'POST':
        return redirect('cloud_form')

    demand_type = 'nova_demanda_cloud' # passa essa informacao no html de nova demanda para referenciar essa rota de cloud quando for acionada
    return render_template("general/novaDemanda.html", data=demand_type)


@blp.route('/processar_form_cloud', methods=['GET','POST'])
def processar_form():
    
    if request.method == 'POST':
        form = CloudModel(**dict(request.form))

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

        try:
            db.session.add(form)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(e)

    return "retornar a pagina do formulario ou a inicial"


# @blp.route('/ver_bd')
# class VerBd(MethodView):
#     @blp.response(200, CloudSchema(many=True)) # Decorator
#     def get(self):
#         return CloudModel.query.all()
