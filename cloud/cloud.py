from flask.views import MethodView
from flask_smorest import abort, Blueprint
from flask import render_template, request, url_for
from models import CloudModel
from sqlalchemy.exc import SQLAlchemyError
from db import db

blp = Blueprint("Cloud", __name__, template_folder='templates' )

@blp.route('/cloud_form')
def get():
    return render_template("cloud/cloud_view.html")


@blp.route('/processar_form_cloud', methods=['POST'])
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
