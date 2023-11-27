from fastapi import HTTPException
import ormar
from functools import wraps

#Decorator é uma função que recebe outra função como parâmetro, trazendo uma outra funcionalidade.
#Podemos manipular a função, para saber qual momento estamos na execução,
#durante o começo da execução, antes e após.
def entidade_nao_encontrada(func):
    @wraps(func)
    async def inner(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except ormar.exceptions.NoMatch:
            raise HTTPException(status_code=404, detail="Entidade não encontrada")
    return inner
#HTTPExceptions, onde passamos o código de retorno e sua mensagem, sendo assim podemos utilizar em todas as ações, não necessitando de grande repetição.
#@wraps, solicita todos os metadatos da minha função de origem.
#args (solicitação de listas)e kwargs(dicionário, acessando por chaves) são variáveis genéricas.

    