from db import db

# Modelo para criar o banco de dados de Itens
class NetworkModel(db.Model):
    __tablename__ = "network"

    # Colunas especificas da area de Network
    requestIdNetwork = db.Column(db.Integer, primary_key=True)
    inputNetworkActivity = db.Column(db.String(80), nullable=True)
    inputSitesDemand = db.Column(db.Text, nullable=True)
    radioPsr = db.Column(db.String(25), nullable=True)

    # Campos que serão preenchidos dependendo do resultado do radioPsr(Previous Service Request)
    inputIDs = db.Column(db.String(80), nullable=True)

    # Colunas especificas da area de Network - apos a escolha do radioPsr
    inputHLD = db.Column(db.String(80), nullable=True)

    # Relacionamento com a tabela request
    requestIdFk = db.Column(db.Integer, db.ForeignKey('requests.requestId'), nullable=False)


    
    
    


