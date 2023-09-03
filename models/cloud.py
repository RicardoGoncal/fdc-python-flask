from db import db

# Modelo para criar o banco de dados de Itens
class CloudModel(db.Model):
    __tablename__ = "cloud"
    
    # Colunas especificas da area de Cloud
    requestIdCloud = db.Column(db.Integer, primary_key=True)
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

    # Colunas especificas da area de Cloud  - Apos a escolha do radioRg
    radioSp = db.Column(db.String(25), nullable=True)
    inputHLD = db.Column(db.String(80), nullable=True)
    inputFunctionArea = db.Column(db.String(80), nullable=True)
    inputAzureResources = db.Column(db.String(80), nullable=True)
    radioNet = db.Column(db.String(25), nullable=True)
    inputDescribeConfig = db.Column(db.Text, nullable=True)

    # Relacionamento com a tabela request
    # requestIdFk = db.Column(db.Integer, db.ForeignKey('requests.requestId'), nullable=False)

    cloudIdFk = db.relationship("RequestModel", backref="cloud", lazy=True)



