from db import db

# Modelo para criar o banco de dados de Itens
class RequestModel(db.Model):
    __tablename__ = "requests"
    # Campos comuns de qualquer demanda
    requestId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # Estabelecer o tipo de Demanda Aberta
    demandType = db.Column(db.String(80), nullable=False)
    # Continuação dos campos comuns
    inputPPM = db.Column(db.Integer, nullable=True)
    inputTypeCust = db.Column(db.String(80), nullable=True)
    inputProjectDemandName = db.Column(db.String(80), nullable=True)
    inputDemandPEPCC = db.Column(db.String(80), nullable=True)
    inputManager = db.Column(db.String(80), nullable=True)
    inputArchitect = db.Column(db.String(80), nullable=True)
    inputEntityResposible = db.Column(db.String(80), nullable=True)
    inputItOt = db.Column(db.String(80), nullable=True)
    inputSpecialReq = db.Column(db.String(80), nullable=True)
    inputHelpText = db.Column(db.Text, nullable=True)

    # Chaves Estrangeiras - Relação de tabelas Requests com qualquer outra
    # requestIdCloud = db.Column(db.Integer, db.ForeignKey('cloud.requestIdCloud'), nullable=False)

    cloudIdFk = db.relationship("CloudModel", backref="requests", lazy=True)
    networkIdFk = db.relationship("NetworkModel", backref="requests", lazy=True)
    # networkIdFk = db.relationship("NetworkModel", back_populates="networkItem", lazy="dynamic", cascade="all, delete")