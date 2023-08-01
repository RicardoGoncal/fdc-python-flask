from marshmallow import Schema, fields

"""
Area destinada a criar um esquema de definicao dos parametros que 
serao recebidos via body de um POST ou URL de um GET
"""


"""
Esquema modelo para iniciar qualquer formulario do FDC,
pois são itens comuns para todos
"""
class PlainFdcSchema(Schema):
    request_id = fields.Int(dump_only=True)
    nome_requisitor = fields.Str(required=True)
    disciplina = fields.Str(required=True)


"""
Esquema para itens exclusivos de abertura de chamado Cloud
"""
class CloudSchema(PlainFdcSchema):
    nome_do_rg = fields.Str(required=True)