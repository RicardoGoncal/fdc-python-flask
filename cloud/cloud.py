from flask.views import MethodView
from flask_smorest import abort, Blueprint
from flask import render_template, request, url_for
from schemas import CloudSchema
from models import CloudModel
from sqlalchemy.exc import SQLAlchemyError
from db import db

blp = Blueprint("Cloud", __name__, template_folder='templates' )

@blp.route('/cloud_form')
def get():
    return render_template("cloud/cloud_view.html")


@blp.route('/processar_form', methods=['POST'])
def processar_form():

    form = CloudModel(**dict(request.form))

    # form = CloudModel(**form)

    try:
        print(form)
        db.session.add(form)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(e)

    return "retornar a pagina do formulario ou a inicial"


@blp.route('/ver_bd')
class VerBd(MethodView):
    @blp.response(200, CloudSchema(many=True)) # Decorator
    def get(self):
        return CloudModel.query.all()
