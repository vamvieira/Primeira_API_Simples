import ormar
import re
from pydantic import validator
from sqlalchemy.sql.expression import table
from config import database, metadata

#re = regex => Como uma linguagem de progamação é feita, uma função que permite localizar padrões em textos
class Papel(ormar.Model):
    class Meta:
        metadata = metadata
        database = database
        tablename = "papeis"

#informar ao ormar que é inteiro, por isso utiliza o Integer
    id: int = ormar.Integer(primary_key=True)
    nome: str = ormar.String(max_length=100)
    sigla: str = ormar.String(max_length=10)
    cnpj: str = ormar.String(max_length=20)
    
#criar validador para a sigla do papel
#'^[A-Z]{4}-(Repetições letras maiúsculas de A a Z, 4 vezes). [0-9]{1,2}-(Repetições entre 0 e 9, entre um a dois numeros)'
    @validator('sigla')
    def valida_formatacao_sigla(cls, v):
        if not re.compile('^[A-Z]{4}[0-9]{1,2}$').match(v):
            raise ValueError('A sigla do papel é inválida!')
        return v

#raise diz que é um resultado esperado de um erro
