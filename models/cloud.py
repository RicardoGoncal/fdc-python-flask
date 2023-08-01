from db import db

# Modelo para criar o banco de dados de Itens
class CloudModel(db.Model):
    __tablename__ = "cloud"

    request_id = db.Column(db.Integer, primary_key=True)
    nome_requisitor = db.Column(db.String(80), unique=True, nullable=False)
    disciplina = db.Column(db.String(80), unique=True, nullable=False)
    nome_do_rg = db.Column(db.String(80), unique=True, nullable=False)
  




