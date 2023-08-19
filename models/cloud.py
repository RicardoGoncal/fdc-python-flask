from db import db

# Modelo para criar o banco de dados de Itens
class CloudModel(db.Model):
    __tablename__ = "cloud"

    # request_id = db.Column(db.Integer, primary_key=True)
    # nome_requisitor = db.Column(db.String(80), nullable=False)
    # disciplina = db.Column(db.String(80), nullable=False)
    # nome_do_rg = db.Column(db.String(80), nullable=False)
    
    # Campos comuns parte 1 - Antes da escolha do radioRg
    requestId = db.Column(db.Integer, primary_key=True)
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
    radioRg = db.Column(db.String(25), nullable=True)

    # Campos que serão preenchidos dependendo do resultado do radioRg(Existe ou nao um RG)
    inputResourceGroup = db.Column(db.String(80), nullable=True)
    inputNeedUsersAccess = db.Column(db.String(80), nullable=True)
    inputProjectName = db.Column(db.String(80), nullable=True)
    inputResponsible = db.Column(db.String(80), nullable=True)
    inputWorkType = db.Column(db.String(80), nullable=True)
    inputRegion = db.Column(db.String(80), nullable=True)
    radioTransition = db.Column(db.String(50), nullable=True)
    inputDate = db.Column(db.Date, nullable=True)

    # Campos comuns parte 2 - Apos a escolha do radioRg
    radioSp = db.Column(db.String(25), nullable=True)
    inputHLD = db.Column(db.String(80), nullable=True)
    inputFunctionArea = db.Column(db.String(80), nullable=True)
    inputAzureResources = db.Column(db.String(80), nullable=True)
    radioNet = db.Column(db.String(25), nullable=True)
    inputDescribeConfig = db.Column(db.Text, nullable=True)



