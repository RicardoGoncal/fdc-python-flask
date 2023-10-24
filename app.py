from flask import Flask
from flask_migrate import Migrate
from general.general import blp as GeneralBlueprint
from cloud.cloud import blp as CloudBlueprint
from network.network import blp as NetworkBlueprint

from db import db
import os
from dotenv import load_dotenv


def create_app(db_url=None):
    app = Flask(__name__)
    load_dotenv()

    app.debug = True
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db") # Usa a conexao de banco desejada, mas o default seria o sqlite
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True
    # app.config["SECRET_KEY"] = "hello_world"

    db.init_app(app) # Inicia o contexto do banco de dados com o app criado

    # migrate = Migrate(app, db)
  
    # # Se utilizado o Migrate, não precisa usar esse comando
    with app.app_context():
        db.create_all()    # Quando se inicia, ele cria o banco de acordo com os modelos criados na pasta models

    app.register_blueprint(CloudBlueprint)
    app.register_blueprint(GeneralBlueprint)
    app.register_blueprint(NetworkBlueprint)
  
    return app