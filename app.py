from flask import Flask, jsonify
from flask_migrate import Migrate
from general.homepage import blp as HomeBlueprint

from db import db
import os


def create_app(db_url=None):
    app = Flask(__name__)

    # db.init_app(app) # Inicia o contexto do banco de dados com o app criado

    # migrate = Migrate(app, db)
  
    # # Se utilizado o Migrate, não precisa usar esse comando
    # with app.app_context():
    #     db.create_all()    # Quando se inicia, ele cria o banco de acordo com os modelos criados na pasta models

    # app.register_blueprint(CloudBlueprint)
    app.register_blueprint(HomeBlueprint)
  
    return app